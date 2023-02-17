import random

import pytest
from selenium.common import NoSuchElementException, TimeoutException
from behave import step
from PageObject.URLs import Urls
from PageObject.base_page import BasePage
from PageObject.data import RegistrationCreds
from PageObject.locators import LoginPageLocators, MainPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


class LoginPage(BasePage):
    # def __init__(self, browser):
    #     super().__init__(browser)
    #     #self.email = RegistrationCreds.REGISTRATION_EMAIL
    #     self.password = RegistrationCreds.PASSWORD
    def account_page(self):
        self.browser.find_element(*MainPageLocators.MY_ACCOUNT_BUTTON).click()

    def login_page(self):
        self.browser.get(Urls.REACT_MAIN_PAGE)

    def common_user_registration(self):
        self.browser.find_element(*LoginPageLocators.SIGN_UP_EMAIL).send_keys(
            RegistrationCreds.REGISTRATION_EMAIL_ONE)
        self.browser.find_element(*LoginPageLocators.SIGN_UP_PASSWORD).send_keys(
            RegistrationCreds.PASSWORD)
        self.browser.find_element(*LoginPageLocators.SIGN_UP_CONFIRM_PASSWORD).send_keys(
            RegistrationCreds.PASSWORD)
        self.browser.find_element(*LoginPageLocators.FIRST_NAME).send_keys(
            RegistrationCreds.FIRST_NAME
        )
        self.browser.find_element(*LoginPageLocators.LAST_NAME).send_keys(
            RegistrationCreds.LAST_NAME
        )

        # self.reg_hello_message_check()

    def sign_up_button(self):
        self.browser.find_element(*LoginPageLocators.SIGN_UP_BUTTON).click()

    def signin_button(self):
        self.browser.find_element(*LoginPageLocators.SIGN_IN_BUTTON).click()

    def user_login(self, email, password):
        self.browser.find_element(*LoginPageLocators.SiGN_IN_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.SIGN_IN_PASSWORD).send_keys(password)
        self.signin_button()

    def common_user_logout(self):
        self.browser.find_element(*MainPageLocators.USER_MY_ACCOUNT_BUTTON).click()
        self.browser.find_element(*MainPageLocators.LOGOUT_BUTTON).click()

    def login_after_registration(self):
        self.browser.get(Urls.REACT_MAIN_PAGE)
        self.common_user_logout()
        self.account_page()
        self.browser.find_element(*LoginPageLocators.SiGN_IN_EMAIL).send_keys(
            RegistrationCreds.REGISTRATION_EMAIL_ONE)
        self.browser.find_element(*LoginPageLocators.SIGN_IN_PASSWORD).send_keys(
            RegistrationCreds.PASSWORD)
        self.browser.find_element(*LoginPageLocators.SIGN_IN_BUTTON).click()

    def forgot_password_login_page(self, email):
        self.browser.find_element(*LoginPageLocators.FORGOT_PASSWORD_LINK).click()
        self.browser.find_element(*LoginPageLocators.RESET_PASSWORD_FIELD).send_keys(email)
        print(f'3:\n{email}')
        self.browser.find_element(*LoginPageLocators.RESET_PASSWORD_SUBMIT_BTN).click()

    def change_password_from_login_page(self, password):
        link = ReadLettersFromGmail().return_link_for_reset_password()
        self.go_to_url(link)
        self.browser.find_element(*LoginPageLocators.NEW_PASSWORD_RESET_FIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_RESET_FIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.SUBMIT_BUTTON_RESET_PASSWORD).click()

