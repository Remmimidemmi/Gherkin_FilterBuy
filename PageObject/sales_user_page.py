import random
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from syst.URLs import Urls
from PageObject.base_page import BasePage
from syst.data import NewCustomerData, RegistrationCreds
from syst.locators import NewCustomersLocators, MainPageLocators


class SalesUserPage(BasePage):
    def go_to_customers_tab(self):
        self.browser.find_element(*NewCustomersLocators.CUSTOMERS_TAB).click()

    def go_to_mask_user(self):
        self.go_to_customers_tab()
        user = self.browser.find_element(
            *NewCustomersLocators.CUSTOMERS_LIST_NEW_CUSTOMER).text.split('@')[0]
        mask_button = self.browser.find_element(*NewCustomersLocators.MASK_BUTTON)
        self.browser.execute_script(
            "return arguments[0].scrollIntoView(true);", mask_button)
        mask_button.click()
        user_to_mask = self.browser.find_element(
            *NewCustomersLocators.HELLO_BUSINESS_USER_TEXT).text[7:-1]
        current_link = self.browser.current_url
        assert user_to_mask == user \
               and current_link == Urls.REACT_MASK_BUSINESS_USER, \
            f"Mask unsuccessful!\nUser to mask:\n{user_to_mask}\nUser:\n{user}\nLink:\n{current_link}"
        print(f"Redirect on link:\n{current_link}\nto mask business user:\n{user}!")

    def go_to_customer_details(self):
        self.go_to_customers_tab()
        user_to_details = self.browser.find_element(
            *NewCustomersLocators.CUSTOMERS_LIST_CUSTOMER_NAME).text
        details_button = self.browser.find_element(
            *NewCustomersLocators.CUSTOMER_DETAILS_BUTTON)
        self.browser.execute_script(
            "return arguments[0].scrollIntoView(true);", details_button)
        details_button.click()
        user_from_details = self.browser.find_element(
            *NewCustomersLocators.USER_NAME_FROM_DETAILS).text
        customer_information = self.browser.find_element(
            *NewCustomersLocators.CUSTOMER_INFORMATION_INSCR).text
        assert user_to_details == user_from_details, f"Details button doesn't work correctly!" \
                                                     f"\n{user_from_details}\n!=\n{user_to_details}"
        print(f"\nDetails button work correctly:\n{customer_information}\n{user_to_details} == {user_from_details}")

    def new_customer_email_one(self):
        self.browser.find_element(*NewCustomersLocators.EMAIL).send_keys(NewCustomerData.CUSTOMER_EMAIL_ONE)

    def new_customer_email_two(self):
        self.browser.find_element(*NewCustomersLocators.EMAIL).send_keys(NewCustomerData.CUSTOMER_EMAIL_TWO)

    def new_customer_incorrect_email(self):
        self.browser.find_element(*NewCustomersLocators.EMAIL).send_keys(RegistrationCreds.INCORRECT_REGISTRATION_EMAIL)

    def go_to_sales_user(self):
        self.browser.find_element(*MainPageLocators.USER_MY_ACCOUNT_BUTTON).click()
        # acc_btn = WebDriverWait(self.browser, 5).until(
        #     EC.element_to_be_clickable(MainPageLocators.USER_MY_ACCOUNT_BUTTON)
        # )
        # acc_btn.click()
        sales_btn = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(MainPageLocators.SALES_LINK_TAB)
        )
        sales_btn.click()
        # self.browser.find_element(*MainPageLocators.SALES_LINK_TAB).click()

    def new_customer_information(self):
        user_name = "PoguCo" + str(random.randint(1, 99999))
        self.browser.find_element(*NewCustomersLocators.BUSINESS_NAME).send_keys(user_name)
        self.browser.find_element(*NewCustomersLocators.TAX_EXEMPT_CHECKBOX).click()
        self.browser.find_element(*NewCustomersLocators.CREDIT_TERMS_CHECKBOX).click()

    def new_main_contact(self):
        self.browser.find_element(*NewCustomersLocators.FIRST_NAME).send_keys(RegistrationCreds.FIRST_NAME)
        self.browser.find_element(*NewCustomersLocators.LAST_NAME).send_keys(RegistrationCreds.LAST_NAME)
        self.browser.find_element(*NewCustomersLocators.PHONE_NUMBER).click()
        self.browser.find_element(*NewCustomersLocators.PHONE_NUMBER).send_keys(NewCustomerData.PHONE_NUMBER)

    def new_shipping_address(self):
        self.browser.find_element(*NewCustomersLocators.COMPANY_NAME).send_keys(NewCustomerData.BUSINESS_NAME)
        self.browser.find_element(*NewCustomersLocators.ATTN).send_keys(NewCustomerData.ATTN)
        self.browser.find_element(*NewCustomersLocators.STREET_ADDRESS).send_keys(NewCustomerData.STREET_ADDRESS)
        self.browser.find_element(*NewCustomersLocators.TOWN_CITY).send_keys(NewCustomerData.TOWN_CITY)
        self.browser.find_element(*NewCustomersLocators.STATE).send_keys(NewCustomerData.STATE)
        self.browser.find_element(*NewCustomersLocators.STATE).send_keys(Keys.ENTER)
        self.browser.find_element(*NewCustomersLocators.POSTCODE_ZIP).send_keys(NewCustomerData.POSTCODE_ZIP)
        self.browser.find_element(*NewCustomersLocators.STATE).click()

    def submit_button(self):
        self.browser.find_element(*NewCustomersLocators.SUBMIT_CUSTOMER_BTN).click()

    def new_customer_check_one(self):
        email = NewCustomerData.CUSTOMER_EMAIL_ONE
        new_customer_email = self.browser.find_element(*NewCustomersLocators.CUSTOMERS_LIST_NEW_CUSTOMER).text
        assert new_customer_email == email, f"New customer is not found!\n{email}\n" \
                                            f"!=\n{new_customer_email}"
        print(f"\nNew customer:{new_customer_email}\n==\n{email}")

    def new_customer_check_two(self):
        email = NewCustomerData.CUSTOMER_EMAIL_TWO
        new_customer_email = self.browser.find_element(*NewCustomersLocators.CUSTOMERS_LIST_NEW_CUSTOMER).text
        assert new_customer_email == email, f"New customer is not found!\n{email}\n" \
                                            f"!=\n{new_customer_email}"
        print(f"\nNew customer:{new_customer_email}\n==\n{email}")

    def reg_sales_user(self):
        self.browser.find_element(*MainPageLocators.REQUEST_SALES_USER_FIELD).send_keys("Test" + str(
            random.randint(1, 99999)))
        self.browser.find_element(*MainPageLocators.BECOME_SALES_USER_BUTTON).click()

    def user_go_to_send_request_to_sales_account(self):
        self.browser.get(Urls.REACT_REQUEST_NEW_SALES_USER)

    def check_for_success_add_customer_notifier(self):
        exp_notifier = "Customer has been added successfully."
        notifier = WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(
            NewCustomersLocators.ADD_CUSTOMER_NOTI_SUCCESS))
        text_notifier = notifier.text
        assert notifier and text_notifier == exp_notifier, \
            f"Notice missing\nor Expected notice:\n{exp_notifier}\n!=\nActual notice:{text_notifier}"
        print(f'Expected notice:\n{exp_notifier}\n==\nActual notice:\n{text_notifier}')
