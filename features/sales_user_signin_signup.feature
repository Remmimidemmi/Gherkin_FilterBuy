Feature: Sales(LogIn/SignUp)

  Background:
    Given User opens the website: 'FilterBuy'

  @test_1
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

  @test_2
  @fixture.new_browser
  Scenario Outline: User tries to login with incorrect password

    When User click on "My Account" button
      And User fills email: <email>
      And User fills password: <password>
      And User clicks the "Log In" button
    Then User is not logged in and sees an error message
      And Link "reset your password" in the error message is clickable
    Examples:
      |password |      email      |
      |1234     | test1@test.test |



  @test_3
  @fixture.new_browser
  Scenario Outline: User tries to login with incorrect email

    When User click on "My Account" button
      And User fills email: <email>
      And User fills password: <pass>
      And User clicks the "Log In" button
    Then User is not logged in and sees an error message
      And Link "reset your password" in the error message is clickable
    Examples:
      |pass  |      email      |
      |123   | test0@test.test |

  @test_4
  @fixture.new_browser
  Scenario Outline: User tries to login with an empty email

    When User click on "My Account" button
      And User fills password: <password>
      And User clicks the "Log In" button
    Then User can't login with an empty fields
    Examples:
      |password  |
      |123       |

  @test_5
  @fixture.new_browser
  Scenario Outline: User tries to login with an empty password

    When User click on "My Account" button
      And User fills email: <email>
      And User clicks the "Log In" button
    Then User can't login with an empty fields
    Examples:
      |      email      |
      | test1@test.test |

  @test_6
  @fixture.new_browser
  Scenario: User tries to login with all empty fields

    When User click on "My Account" button
      And User clicks the "Log In" button
    Then User can't login with an empty fields

  @test_7
  @fixture.new_browser
  Scenario Outline: User wants to reset their password

    When User click on "My Account" button
      And User clicks "forgot password" button
      And User sends their <email> address for receive the message from filterbuy
      And User goes to their mailbox to follow the link in the message
      And User change the password: <password>
    Then User see a welcome message
    Examples:
      | password | email               |
      | 321      | zast0tsaz@gmail.com |
      | 123      | zast0tsaz@gmail.com |

