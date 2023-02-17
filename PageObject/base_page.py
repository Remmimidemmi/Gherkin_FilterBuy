from selenium.common import NoSuchElementException
from behave import step
import random
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.wait import WebDriverWait

from PageObject.locators import MainPageLocators


class BasePage:
    def __init__(self, browser, timeout=10):
        self.browser = browser
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.browser.current_url)

    def account_page(self):
        self.browser.find_element(*MainPageLocators.MY_ACCOUNT_BUTTON).click()

    def hello_message(self):
        hello_user = self.browser.find_element(*MainPageLocators.HELLO_USERNAME)
        text_hello_user = hello_user.text
        user_name = text_hello_user[7:]
        print(f"Login success!\nHello {user_name}!")
        return user_name

    def reg_hello_message_check(self):
        assert self.hello_message() == RegistrationCreds.FIRST_NAME, "Registration failed!"
        print(f'Registration of {self.hello_message()} correct!')

    def error_message(self, message, exp_message):
        error_message = WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(message))
        text_error_message = error_message.text
        assert text_error_message == exp_message, f"EXPECTED:\n{exp_message}\nACTUAL:\n{text_error_message}"
        print("\nMessage correct!")

    def error_link(self, link):
        error_link = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(link))
        assert error_link, "Link is not clickable!"
        print("Link is clickable!")

    def go_to_url(self, url):
        while True:
            try:
                self.browser.get(url)
                break
            except:
                time.sleep(10)


