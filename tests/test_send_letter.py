import time
from .config_for_tests import login, password, \
    get_random_number, get_random_word, count_of_letters, count_of_numbers
from pages.base_page import BasePage
from pages.message_page import MessagePage


def test_send_mails(browser):
    link = 'https://mail.ru/'
    browser.set_window_size(1920, 1080)
    page = BasePage(browser, link)
    page.open()
    page.go_to_login_page()
    page.login_user(login, password)
    time.sleep(3)
    message_page = MessagePage(browser, browser.current_url)
    message_page.close_calendar_alert()

    amount_of_mails = get_random_number(1, 5)
    mail_list = {}

    for i in range(amount_of_mails):
        theme_temp = get_random_word(10)
        body_temp = get_random_word(10)
        mail_list[theme_temp] = body_temp

        message_page.send_message(login, body_temp, theme_temp)

    message_page.go_to_yourself_messages()

    for theme, body in mail_list.items():
        message_page.is_message_body_present(body)
        message_page.is_message_theme_present(theme)

    final_message = f'Amount_of_mails = {amount_of_mails} \n'
    number_mail = 1
    for theme, body in mail_list.items():
        final_message += f"{number_mail}) Received mail on theme '{theme}' "\
                         f"with message: '{body}'."\
                         f"It contains {count_of_letters(body)} "\
                         f"letters and {count_of_numbers(body)} numbers \n"
        number_mail += 1

    message_page.send_message(login, final_message, 'final_message')

    for theme, body in mail_list.items():
        message_page.delete_received_message(theme)
        message_page.go_to_yourself_messages()








