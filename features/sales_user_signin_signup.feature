Feature: Sales(LogIn/SignUp)

  Background:
    Given User opens the website: 'FilterBuy'

  @fixture.new_browser
  Scenario: User registers a new sales account

    When User click on "My Account" button
      And User enter the data in registration fields
      And User clicks Sign Up button
      And User see a welcome message
      And User goes to the page with sending requests to activate the sales account
      And User sends a request to activate the sales account
      And Admin login into their account
      And Admin approves new sales user
    Then User can login in their new sales account

  @fixture.new_browser
  Scenario: User try to login with incorrect password

    When User click on "My Account" button
      And User fills correct email
      And User fills incorrect password
      And User clicks the "Log In" button
    Then User is not logged in and sees an error message
      And Link "reset password" is clickable
    """Invalid username/password. Please try again. If you have ordered from us previously
                          or created an account, you can also reset your password. """






    #https://admin:admin!2@react.test.filterbuytest.com/my-account/login/?next=/my-account/