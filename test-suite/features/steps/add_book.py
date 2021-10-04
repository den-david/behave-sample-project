from behave import *
from requests import api as request_handler
from faker import Faker

@given('POST Add Book payload is complete')
def step_impl(context):
    faker_data_generator = Faker()
    context.add_book_payload = {
        "name": faker_data_generator.sentence(nb_words=5),
        "isbn": str(faker_data_generator.word()),
        "aisle": str(faker_data_generator.random_int(min=100, max=999)),
        "author": faker_data_generator.name()
    }

@given('POST Add Book payload has {value} value in {field} field')
def step_impl(context, field, value):
    context.execute_steps('Given POST Add Book payload is complete')
    context.add_book_payload[field] = value

@when('POST Add Book is hit using payload')
def step_impl(context):
    context.response = request_handler.post(url=context.target_api_url + "/Library/Addbook.php", json=context.add_book_payload)

@then('POST Add Book Response status code is {code}')
def step_impl(context, code):
    assert context.response.status_code == int(code), f"Response status code is not the same as {code}"

@then('POST Add Book Response data for status code {code} is correct')
def step_impl(context, code):
    if code == "200":
        actual_response = context.response.json()
        expected_response = context.add_book_payload
        assert "Msg" in actual_response, "Msg key is not in response"
        assert actual_response["Msg"] == "successfully added", "Msg value is not correct"
        assert "ID" in actual_response, "ID key is not in response"
        assert actual_response["ID"] == expected_response["isbn"] + expected_response["aisle"], "ID value is not correct"
    elif code == "400":
        # sample code only
        actual_response = context.response.json()
        assert "Msg" in actual_response, "Msg key is not in response"
        assert actual_response["Msg"] == "Bad Request"
    else:
        assert False, "Code is not in any of the options"


@then('POST Add Book handles invalid values')
def step_impl(context):
    for row in context.table:
        context.execute_steps(f'''
            Given POST Add Book payload has {row['value']} value in {row['field']} field
            When POST Add Book is hit using payload
            Then POST Add Book Response status code is 400
            And POST Add Book Response data for status code 400 is correct
        ''')
