from selenium.webdriver.common.by import By


class MainPageLocators:
    MY_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "#hdr-mr > span:nth-child(1) > a > i")
    HELLO_USERNAME = (By.CSS_SELECTOR, "#container > div.account-username > span")
    REQUEST_SALES_USER_FIELD = (By.CSS_SELECTOR, "#id_registration_info")
    BECOME_SALES_USER_BUTTON = (By.CSS_SELECTOR, "button.btn")
    SALES_LINK_TAB = (By.CSS_SELECTOR, "#outside-sales > div:nth-child(1)")
    USER_MY_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "#hdr-mr > span:nth-child(1) > span:nth-child(1)")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "#account-drop-logout > a")


class LoginPageLocators:
    SIGN_UP_EMAIL = (By.CSS_SELECTOR, "#signup-email")
    SIGN_UP_PASSWORD = (By.CSS_SELECTOR, "#signup-password")
    SIGN_UP_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#signup-confirm_password")
    FIRST_NAME = (By.CSS_SELECTOR, "#signup-first_name")
    LAST_NAME = (By.CSS_SELECTOR, "#signup-last_name")
    SIGN_UP_BUTTON = (By.CSS_SELECTOR, "#submit-signup")
    SiGN_IN_EMAIL = (By.CSS_SELECTOR, "#login-email")
    SIGN_IN_PASSWORD = (By.CSS_SELECTOR, "#login-password")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "#submit-login")
    ERROR_LOGIN_MESSAGE = (By.CSS_SELECTOR, "#error-login")
    ERROR_RESET_PASSWORD_MESSAGE = (By.CSS_SELECTOR, "#password-reset-error")
    RESET_PASSWORD_LINK = (By.CSS_SELECTOR, "#reset-your-password")
    FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, "#password-reset")
    SIGN_UP_LINK_AFTER_FORGOT = (By.CSS_SELECTOR, "#password-reset-signup") #reset-your-password
    RESET_PASSWORD_FIELD = (By.CSS_SELECTOR, "#password-reset-email")
    RESET_PASSWORD_SUBMIT_BTN = (By.CSS_SELECTOR, "#password-reset-submit")
    NEW_PASSWORD_RESET_FIELD = (By.CSS_SELECTOR, "#id_new_password1")
    CONFIRM_PASSWORD_RESET_FIELD = (By.CSS_SELECTOR, "#id_new_password2")
    SUBMIT_BUTTON_RESET_PASSWORD = (By.CSS_SELECTOR, "#reset-submit")


class ReactAdminLocators:
    SIGN_IN_EMAIL = (By.CSS_SELECTOR, "#id_username")
    SIGN_IN_PASSWORD = (By.CSS_SELECTOR, "#id_password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#bottombar > button:nth-child(1)")
    FIRST_CHECKBOX_ACTIVE = (By.CSS_SELECTOR, "#id_form-0-active")
    SAVE_BUTTON = (By.CSS_SELECTOR, "#bottombar > button")


class NewCustomersLocators:
    BUSINESS_NAME = (By.CSS_SELECTOR, "#completeName")
    CREDIT_TERMS_CHECKBOX = (By.XPATH, "//*[@id='root']/div[1]/div[3]/div/div/main/div/div/form/div/div/div["
                                       "1]/div[1]/div[1]/label[1]/span[1]/span[1]/input")
    TAX_EXEMPT_CHECKBOX = (By.XPATH, "//*[@id='root']/div[1]/div[3]/div/div/main/div/div/form/div/div/div[1]/div["
                                     "1]/div[1]/label[2]/span[1]/span[1]/input")
    EMAIL = (By.CSS_SELECTOR, "#main_contact\.email")
    FIRST_NAME = (By.CSS_SELECTOR, "#main_contact\.first_name")
    LAST_NAME = (By.CSS_SELECTOR, "#main_contact\.last_name")
    PHONE_NUMBER = (By.XPATH, '//*[@id="main_contact.phone_number"]')
    SUBMIT_CUSTOMER_BTN = (By.XPATH, "/html/body/div[1]/div[4]/div[2]/div[1]/div["
                                     "3]/div/div/main/div/div/form/div/div/div[2]/button")
    COMPANY_NAME = (By.CSS_SELECTOR, "#shipping_address\.company_name")
    ATTN = (By.CSS_SELECTOR, "#shipping_address\.attn")
    STREET_ADDRESS = (By.CSS_SELECTOR, "#shipping_address\.address_line_1")
    TOWN_CITY = (By.CSS_SELECTOR, "#shipping_address\.city")
    STATE = (By.XPATH, '//*[@id="shipping_address.state"]')
    POSTCODE_ZIP = (By.CSS_SELECTOR, "#shipping_address\.postal_code")
    CUSTOMERS_LIST_NEW_CUSTOMER = (By.CSS_SELECTOR, "div.Mui-even:nth-child(1) > div:nth-child(2) > a:nth-child(1)")
    CUSTOMERS_LIST_CUSTOMER_NAME = (By.XPATH, '//*[@id="customersTable"]/div/div[2]/div['
                                                     '2]/div/div/div/div/div/div[1]/div[1]')
    ALABAMA = (By.CSS_SELECTOR, '#shipping_address.state-option-0')
    EMPTY_FIELD_NEW_CUSTOMER_MESSAGE = (By.CSS_SELECTOR, "#completeName-helper-text")
    CUSTOMERS_TAB = (By.XPATH, '//*[@id="appBar"]/nav/a[4]')
    MASK_BUTTON = (By.XPATH, '//*[@id="customersTable"]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div['
                             '5]/span[4]/button')
    HELLO_BUSINESS_USER_TEXT = (By.CSS_SELECTOR, "#account-header")
    CUSTOMER_DETAILS_BUTTON = (By.XPATH, '//*[@id="customersTable"]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div['
                                         '5]/span[1]/a')
    USER_NAME_FROM_DETAILS = (By.XPATH, '//*[@id="root"]/div[1]/div[3]/div/div/main/div/div/div/div[2]/div['
                                        '2]/div/div/div/div[1]/div[2]/div[2]')
    CUSTOMER_INFORMATION_INSCR = (By.XPATH, '//*[@id="root"]/div[1]/div[3]/div/div/main/div/div/div/div[1]/div[1]/h2')


