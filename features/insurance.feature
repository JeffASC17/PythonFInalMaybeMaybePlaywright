Feature: Automobile insurance quote

  Scenario: Enter customer details and proceed to price options
    Given I am on the home page
    When I open the automobile quote page
    Then the vehicle fields should be visible
    When I enter the vehicle details from "VehicleData.csv"
    When I go to Insurant Data
    When I enter Insurant details from "InsurantData.csv"
    When I go to Product Data
    When I enter Product details from "ProductData.csv"
    When I go to Select Price option
    Then I can see the Price Options Table
