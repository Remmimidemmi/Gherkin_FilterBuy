from selenium.webdriver.remote.webdriver import WebDriver
from behave import *

from PageObject.base_page import BasePage
from PageObject.login_page import LoginPage
from PageObject.react_admin_page import ReactAdminPage
from PageObject.sales_user_page import SalesUserPage


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


@step('User goes to the page with sending requests to activate the sales account')
def go_to_request_to_sales(context):
    browser: WebDriver = context.browser
    SalesUserPage(browser).user_go_to_send_request_to_sales_account()


@step('User sends a request to activate the sales account')
def send_request_for_sales(context):
    browser: WebDriver = context.browser
    SalesUserPage(browser).reg_sales_user()


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


@step('User login as sales user')
def login_as_sales_user(context):
    browser: WebDriver = context.browser
    LoginPage(browser).user_login()


@step('User go to sales account')
def user_go_to_sales_account(context):
    browser: WebDriver = context.browser
    SalesUserPage(browser).go_to_sales_user()


@step('User filling customer information in new customer tab')
def user_enter_customer_email(context):
    browser: WebDriver = context.browser
    SalesUserPage(browser).new_customer_information()


@step('User filling customer main contact in new customer tab')
def customer_main_contact_one(context):
    browser: WebDriver = context.browser
    SalesUserPage(browser).new_customer_email_one()
    SalesUserPage(browser).new_main_contact()


@step('User filling customers main contact in new customer tab')
def customer_main_contact_two(context):
    browser: WebDriver = context.browser
    SalesUserPage(browser).new_customer_email_two()
    SalesUserPage(browser).new_main_contact()


@step('User clicks submit button')
def submit_customer_button(context):
    browser: WebDriver = context.browser
    SalesUserPage(browser).submit_button()


@step('New customer displayed in Customers tab')
def check_for_new_customer_one(context):
    browser: WebDriver = context.browser
    SalesUserPage(browser).new_customer_check_one()


@step('New customer displayed in Customer tab')
def check_for_new_customer_two(context):
    browser: WebDriver = context.browser
    SalesUserPage(browser).new_customer_check_two()

@step('Checking for the success notification')
def check_add_customer_notifier(context):
    browser: WebDriver = context.browser
    SalesUserPage(browser).check_for_success_add_customer_notifier()


@step('User filling customer shipping address in new customer tab')
def customer_shipping_address(context):
    browser: WebDriver = context.browser
    SalesUserPage(browser).new_shipping_address()
