from behave import *
from requests import api as request_handler
from faker import Faker
import random

@given('Books have been added to the library')
def step_impl(context):
    context.added_books = []
    author_name = Faker().name()
    context.get_books_param = f"?AuthorName={author_name}"
    for book_count in range(random.randint(1, 5)):
        context.execute_steps(f'Given POST Add Book payload has {author_name} value in author field')
        context.added_books.append(context.add_book_payload)
        context.execute_steps('''
            When POST Add Book is hit using payload
            Then POST Add Book Response status code is 200''')

@when('GET Books is hit')
def step_impl(context):
    context.response = request_handler.get(url=context.target_api_url + "/Library/GetBook.php" + context.get_books_param, json=context.add_book_payload)

@then('GET Books Response status code is {code}')
def step_impl(context, code):
    assert context.response.status_code == int(code), f"Response status code is not the same as {code}"

@then('GET Books Response data for status code {code} is correct')
def step_impl(context, code):
    if code == "200":
        actual_response = context.response.json()
        expected_response = context.added_books
        for book_count in range(len(expected_response)):
            actual_book = actual_response[book_count]
            expected_book = expected_response[book_count]
            assert actual_book["book_name"] == expected_book["name"], f"Book name does not match for book count {book_count}"
            assert actual_book["isbn"] == expected_book["isbn"], f"ISBN does not match for book count {book_count}"
            assert actual_book["aisle"] == expected_book["aisle"], f"Aisle does not match for book count {book_count}"
    elif code == "400":
        actual_response = context.response.json()
        assert "Msg" in actual_response, "Msg key is not in response"
        assert actual_response["Msg"] == "Bad Request"
    else:
        assert False, "Code is not in any of the options"
