import time

from selenium.webdriver.remote.webdriver import WebDriver
from behave import *

from PageObject.base_page import BasePage
from PageObject.login_page import LoginPage
from syst.data import LogInCreds
from syst.inscriptions import ErrorMessages
from syst.locators import LoginPageLocators, MainPageLocators


@step("User opens the website: 'FilterBuy'")
def open_main_page(context):
    browser: WebDriver = context.browser
    LoginPage(browser).main_page()


@step('User click on "My Account" button')
def click_my_account(context):
    browser: WebDriver = context.browser
    BasePage(browser).account_page()


@step("User enter the data in registration fields")
def enter_data_in_register_fields(context):
    browser: WebDriver = context.browser
    LoginPage(browser).common_user_registration()


@step("User clicks Sign Up button")
def click_sign_up(context):
    browser: WebDriver = context.browser
    LoginPage(browser).sign_up_button()


@step("User see a welcome message")
def welcome_message(context):
    browser: WebDriver = context.browser
    LoginPage(browser).hello_message()


@step('User can login in their new sales account')
def login_user_in_new_sales_account(context):
    browser: WebDriver = context.browser
    LoginPage(browser).login_after_registration()


@step('User fills email: {email}')
def user_fills_email(context, email):
    browser: WebDriver = context.browser
    LoginPage(browser).user_login_email(email)


@step('User fills password: {password}')
def user_fills_incorrect_password(context, password):
    browser: WebDriver = context.browser
    LoginPage(browser).user_login_password(password)


@step('User clicks the "Log In" button')
def user_clicks_login_button(context):
    browser: WebDriver = context.browser
    LoginPage(browser).signin_button()


@step('User is not logged in and sees an error message')
def error_message(context):
    browser: WebDriver = context.browser
    BasePage(browser).error_message(LoginPageLocators.ERROR_LOGIN_MESSAGE, ErrorMessages.LOGIN_ERROR_MESSAGE)


@step('Link "reset your password" in the error message is clickable')
def error_link(context):
    browser: WebDriver = context.browser
    BasePage(browser).error_link(LoginPageLocators.RESET_PASSWORD_LINK)


@step("User can't login with an empty fields")
def user_cant_see_welcome_message(context):
    browser: WebDriver = context.browser
    BasePage(browser).verify_element_is_hided(MainPageLocators.HELLO_USERNAME)


@step('User clicks "forgot password" button')
def user_click_forgot_password(context):
    browser: WebDriver = context.browser
    LoginPage(browser).forgot_password_login_page()


@step('User sends their {email} address for receive the message from filterbuy')
def send_email_for_message_from_filterbuy(context, email):
    browser: WebDriver = context.browser
    LoginPage(browser).send_email_to_forgot_password_field(email)
    time.sleep(5)


@step('User goes to their mailbox to follow the link in the message')
def going_to_mailbox_for_read_message(context):
    browser: WebDriver = context.browser
    LoginPage(browser).goes_to_mailbox()


@step('User change the password: {password}')
def change_forgot_password(context, password):
    browser: WebDriver = context.browser
    LoginPage(browser).send_pass_for_reset_forgot_password(password)