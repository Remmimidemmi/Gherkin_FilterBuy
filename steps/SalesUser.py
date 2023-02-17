from selenium.webdriver.remote.webdriver import WebDriver
from behave import *

from PageObject.URLs import Urls
from PageObject.base_page import BasePage
from PageObject.login_page import LoginPage
from PageObject.react_admin_page import ReactAdminPage
from PageObject.sales_user import SalesUser


@step("User opens the website: 'FilterBuy'")
def open_main_page(context):
    browser: WebDriver = context.browser
    LoginPage(browser).login_page()


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


@step('User goes to the page with sending requests to activate the sales account')
def go_to_request_to_sales(context):
    browser: WebDriver = context.browser
    SalesUser(browser).user_go_to_send_request_to_sales_account()


@step('User sends a request to activate the sales account')
def send_request_for_sales(context):
    browser: WebDriver = context.browser
    SalesUser(browser).reg_sales_user()


@step('Admin login into their account')
def admin_log_in(context):
    browser: WebDriver = context.browser
    ReactAdminPage(browser).login_admin()


@step('Admin approves new sales user')
def activate_sales_account(context):
    browser: WebDriver = context.browser
    ReactAdminPage(browser).activate_checkbox_from_outside_salers()


@step('User can login in their new sales account')
def login_user_in_new_sales_account(context):
    browser: WebDriver = context.browser
    LoginPage(browser).login_after_registration()


