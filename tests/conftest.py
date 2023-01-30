from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
import time


@pytest.fixture(scope="function")
def browser(request):
    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    time.sleep(6)
    browser.quit()
