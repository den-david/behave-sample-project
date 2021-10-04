@get_books
Feature: Get Books

  Scenario: Get books successfully
    Given Books have been added to the library
    When GET Books is hit
    Then GET Books Response status code is 200
    And GET Books Response data for status code 200 is correct