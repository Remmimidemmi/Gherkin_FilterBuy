from selenium.webdriver.remote.webdriver import WebDriver
from behave import *

from PageObject.URLs import Urls
from PageObject.login_page import LoginPage


# @step("User opens the website: 'FilterBuy'")
# def open_main_page(context):
#     browser: WebDriver = context.browser
#     browser.get(Urls.REACT_MAIN_PAGE)