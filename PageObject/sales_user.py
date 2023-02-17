import random
import time

from behave import step
from selenium.webdriver.remote.webdriver import WebDriver
from PageObject.URLs import Urls
from PageObject.base_page import BasePage
from PageObject.locators import MainPageLocators


# class SalesUser(BasePage):
#     @step('User sends a request to activate the sales account')
#     def reg_sales_user(self):
#         time.sleep(5)
#         self.browser.find_element(*MainPageLocators.REQUEST_SALES_USER_FIELD).send_keys("Test" + str(
#             random.randint(1, 99999)))
#         self.browser.find_element(*MainPageLocators.BECOME_SALES_USER_BUTTON).click()

    # @step('User goes to the page with sending requests to activate the sales account')
    # def user_go_to_send_request_to_sales_account(self):
    #     self.browser.get(Urls.REACT_REQUEST_NEW_SALES_USER)
