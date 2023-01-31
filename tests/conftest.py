from selenium import webdriver
import pytest


@pytest.fixture(scope="function")
def browser():
    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
