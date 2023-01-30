from pages.base_page import BasePage
from locators.locators import MessagePageLocators
from selenium.webdriver.common.keys import Keys
import time


class MessagePage(BasePage):
    def check_email(self, login):
        try_calendar_alert = self.browser.find_element(*MessagePageLocators.TRY_CALENDAR_ALERT)
        try_calendar_alert.click()

        #check_email = self.browser.find_element(*MessagePageLocators.CHECK_EMAIL)
        #assert check_email.get_atribute("span") == login, f'Login failed'

    def send_message(self, login, message, theme):
        write_message_button = self.browser.find_element(*MessagePageLocators.WRITE_MESSAGE_BUTTON)
        write_message_button.click()

        receiver_field = self.browser.find_element(*MessagePageLocators.RECEIVER_FIELD)
        receiver_field.send_keys(login)

        theme_field = self.browser.find_element(*MessagePageLocators.THEME_FIELD)
        theme_field.send_keys(theme)

        body_field_to_clear = self.browser.find_element(*MessagePageLocators.BODY_FIELD_TO_CLEAR)
        body_field_to_clear.clear()

        body_field = self.browser.find_element(*MessagePageLocators.BODY_FIELD)
        body_field.click()
        body_field.send_keys(message)

        send_message_button = self.browser.find_element(*MessagePageLocators.SEND_MESSAGE_BUTTON)
        send_message_button.click()

        close_button = self.browser.find_element(*MessagePageLocators.CLOSE_BUTTON)
        close_button.click()

    def check_mails_delivered(self):
        to_myself_button = self.browser.find_element(*MessagePageLocators.TO_MYSELF_BUTTON)
        to_myself_button.click()

        theme_in_message = self.browser.find_elements(*MessagePageLocators.THEME_IN_MESSAGE)

        for i in theme_in_message:
            print(f'theme_i = {i.get_attribute("span")}')

        #to_myself_button.get_attribute("span")






