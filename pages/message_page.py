from pages.base_page import BasePage
from locators.locators import MessagePageLocators
from selenium.webdriver.common.by import By


class MessagePage(BasePage):
    def close_calendar_alert(self):
        try_calendar_alert = self.browser.find_element(*MessagePageLocators.TRY_CALENDAR_ALERT)
        try_calendar_alert.click()

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

    def go_to_yourself_messages(self):
        to_myself_button = self.browser.find_element(*MessagePageLocators.TO_MYSELF_BUTTON)
        to_myself_button.click()

    def is_message_theme_present(self, theme):
        assert self.is_element_present(By.XPATH, f"//span[text() = '{theme}']"), \
            f"Theme '{theme}' in messages is not presented, but should be"

    def is_message_body_present(self, body):
        assert self.is_element_present(By.XPATH, f"//span[text() = '{body}']"), \
            f"Body '{body}' in messages is not presented, but should be"

    def delete_received_message(self, theme):
        message = self.browser.find_element(By.XPATH, f"//span[text() = '{theme}']")
        message.click()
        delete_message_button = self.browser.find_element(*MessagePageLocators.DELETE_MESSAGE_BUTTON)
        delete_message_button.click()















