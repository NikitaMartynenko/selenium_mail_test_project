import time
import random
import string
from .config_for_tests import login, password, get_random_word

from pages.base_page import BasePage
from pages.message_page import MessagePage


def test_send_letter(browser):
    link = 'https://mail.ru/'
    browser.set_window_size(1920, 1080)
    page = BasePage(browser, link)
    page.open()
    page.go_to_login_page()

    page.login_user(login, password)

    time.sleep(3)
    print(f'browser.current_url = {browser.current_url}')
    message_page = MessagePage(browser, browser.current_url)
    message_page.check_email(login)
    time.sleep(5)

    amount_of_messages = random.randint(1,5)
    message_list = []
    theme_list = []
    for i in range(amount_of_messages):
        message = get_random_word(10)
        theme = get_random_word(10)
        message_page.send_message(login, message, theme)

        message_list.append(message)
        theme_list.append(theme)

    message_page.go_to_yourself_messages()

    for i in range(amount_of_messages):
        message_page.is_message_body_present(message_list[i])
        message_page.is_message_theme_present(theme_list[i])




