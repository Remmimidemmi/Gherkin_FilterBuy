Feature: New Customer

  Background:
    Given User login as sales user

  @fixture.new_browser
  Scenario: Registration a new customer without a shipping address
    When User go to sales account
      And User filling customer information in new customer tab
      And User filling customer main contact in new customer tab
      And User clicks submit button
    Then Checking for the success notification
      And New customer displayed in Customers tab


  @fixture.new_browser
  Scenario: Registration a new customer with a shipping address
    When User go to sales account
      And User filling customer information in new customer tab
      And User filling customers main contact in new customer tab
      And User filling customer shipping address in new customer tab
      And User clicks submit button
    Then Checking for the success notification
      And New customer displayed in Customer tab

