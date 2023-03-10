from selenium.common.exceptions import NoSuchElementException
from locators.locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def login_user(self, login, password):
        iframe_1 = self.browser.find_element(*BasePageLocators.IFRAME_1)
        self.browser.switch_to.frame(iframe_1)

        login_field = self.browser.find_element(*BasePageLocators.LOGIN_FIELD)
        login_field.send_keys(login)

        remember_me_checkbox = self.browser.find_element(*BasePageLocators.REMEMBER_ME_CHECKBOX)
        remember_me_checkbox.click()

        enter_password_button = self.browser.find_element(*BasePageLocators.ENTER_PASSWORD_BUTTON)
        enter_password_button.click()

        password_field = self.browser.find_element(*BasePageLocators.PASSWORD_FIELD)
        password_field.send_keys(password)

        enter_button = self.browser.find_element(*BasePageLocators.ENTER_BUTTON)
        enter_button.click()
