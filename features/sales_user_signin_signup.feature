Feature: Sales(LogIn/SignUp)
  @fixture.new_browser
  Scenario: The user registers a new sales account
    Given User opens the website: 'FilterBuy'

    When User click on "My Account" button
      And User enter the data in registration fields
      And User clicks Sign Up button
      And User see a welcome message
      And User goes to the page with sending requests to activate the sales account
      And User sends a request to activate the sales account
      And Admin login into their account
      And Admin approves new sales user
    Then User can login in their new sales account




    #https://admin:admin!2@react.test.filterbuytest.com/my-account/login/?next=/my-account/