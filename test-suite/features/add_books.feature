@add_book
Feature: Add Book

  Scenario: Add book successfully
    Given POST Add Book payload is complete
    When POST Add Book is hit using payload
    Then POST Add Book Response status code is 200
    And POST Add Book Response data for status code 200 is correct

  # sample scenario for invalid field values
  # Scenario: Add book with invalid values
    # Then POST Add Book handles invalid values
    #   | field  | value           |
    #   | name   | invalid_value_1 |
    #   | name   | invalid_value_2 |
    #   | name   | invalid_value_3 |
    #   | isbn   |                 |
    #   | aisle  |                 |
    #   | author |                 |