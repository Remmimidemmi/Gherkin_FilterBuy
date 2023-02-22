from selenium.webdriver.remote.webdriver import WebDriver
from behave import *

from PageObject.base_page import BasePage
from PageObject.login_page import LoginPage
from PageObject.react_admin_page import ReactAdminPage
from PageObject.sales_user_page import SalesUserPage
from syst.data import NewCustomerData


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
def customer_main_contact(context):
    browser: WebDriver = context.browser
    SalesUserPage(browser).new_customer_email(NewCustomerData.CUSTOMER_EMAIL_ONE)
    SalesUserPage(browser).new_main_contact()


@step('User filling customers main contact in new customer tab')
def customer_main_contact(context):
    browser: WebDriver = context.browser
    SalesUserPage(browser).new_customer_email(NewCustomerData.CUSTOMER_EMAIL_TWO)
    SalesUserPage(browser).new_main_contact()


@step('User clicks submit button')
def submit_customer_button(context):
    browser: WebDriver = context.browser
    SalesUserPage(browser).submit_button()


@step('New customer displayed in Customers tab')
def check_for_new_customer(context):
    browser: WebDriver = context.browser
    SalesUserPage(browser).new_customer_check(NewCustomerData.CUSTOMER_EMAIL_ONE)


@step('New customer displayed in Customer tab')
def check_for_new_customer(context):
    browser: WebDriver = context.browser
    SalesUserPage(browser).new_customer_check(NewCustomerData.CUSTOMER_EMAIL_TWO)


@step('Checking for the success notification')
def check_add_customer_notifier(context):
    browser: WebDriver = context.browser
    SalesUserPage(browser).check_for_success_add_customer_notifier()


@step('User filling customer shipping address in new customer tab')
def customer_shipping_address(context):
    browser: WebDriver = context.browser
    SalesUserPage(browser).new_shipping_address()

