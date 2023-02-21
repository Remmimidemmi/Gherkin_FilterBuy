from syst.URLs import Urls
from syst.data import AdminCreds, LogInCreds
from PageObject.base_page import BasePage
from syst.locators import ReactAdminLocators


class ReactAdminPage(BasePage):

    def login_admin(self):
        self.browser.get(Urls.ADMIN_OUTSIDE_USERS)
        self.browser.find_element(*ReactAdminLocators.SIGN_IN_EMAIL).send_keys(
            AdminCreds.REACT_ADMIN
        )
        self.browser.find_element(*ReactAdminLocators.SIGN_IN_PASSWORD).send_keys(
            LogInCreds.SIGN_IN_PASSWORD
        )
        self.browser.find_element(*ReactAdminLocators.LOGIN_BUTTON).click()

    def activate_checkbox_from_outside_salers(self):
        self.browser.find_element(*ReactAdminLocators.FIRST_CHECKBOX_ACTIVE).click()
        self.browser.find_element(*ReactAdminLocators.SAVE_BUTTON).click()




