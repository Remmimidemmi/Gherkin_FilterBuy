from selenium.webdriver.remote.webdriver import WebDriver
from behave import *

from PageObject.base_page import BasePage
from PageObject.login_page import LoginPage
from syst.data import LogInCreds
from syst.inscriptions import ErrorMessages
from syst.locators import LoginPageLocators


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


@step('User fills correct email')
def user_fills_email(context):
    browser: WebDriver = context.browser
    LoginPage(browser).user_login_email(LogInCreds.SIGN_IN_EMAIL)


@step('User fills incorrect password')
def user_fills_incorrect_password(context):
    browser: WebDriver = context.browser
    LoginPage(browser).user_login_password(LogInCreds.SIGN_IN_PASSWORD_INCORRECT)


@step('User clicks the "Log In" button')
def user_clicks_login_button(context):
    browser: WebDriver = context.browser
    LoginPage(browser).signin_button()


@step('User is not logged in and sees an error message')
def error_message(context):
    browser: WebDriver = context.browser
    BasePage(browser).error_message(LoginPageLocators.ERROR_LOGIN_MESSAGE, ErrorMessages.LOGIN_ERROR_MESSAGE)


@step('Link "reset password" is clickable')
def error_link(context):
    browser: WebDriver = context.browser
    BasePage(browser).error_link(LoginPageLocators.RESET_PASSWORD_LINK)
