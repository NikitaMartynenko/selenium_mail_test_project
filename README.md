# selenium_mail_test_project
## Выполнение тестового задания с применением Python + Selenium Webdriver.
## Задание:
+ Login to any email box
+ Send from mails from current box to yourself with: Theme: Random string with 10 symbols (letters and numbers only) Body: Random string with 10 symbols (letters and numbers only)
+ Check that all mails are delivered.
+ Collect data from all incoming mails and save it as Object (Dictionary), where: Key is theme of mail Value is body of mail
+ Send collected data to yourself as: “Received mail on theme {Theme} with message: {Body}. It contains {Count of letters} letters and {Count of numbers} numbers” (repeat for each mail)
+ Delete all received mails except the last one

## Копирование репозитория и установка зависимостей.
git clone https://github.com/NikitaMartynenko/selenium_mail_test_project

pip install -r requirements.txt

## Запуск тестов.
cd tests

pytest -s -v --tb=line test_send_letter.py



