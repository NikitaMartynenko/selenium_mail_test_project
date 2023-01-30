from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "[data-testid='enter-mail-primary']")

    IFRAME_1 = (By.CSS_SELECTOR, ".ag-popup__frame__layout iframe")

    LOGIN_FIELD = (By.CSS_SELECTOR, "[name='username']")
    REMEMBER_ME_CHECKBOX = (By.CSS_SELECTOR, "div.box-0-2-111")
    ENTER_PASSWORD_BUTTON = (By.CSS_SELECTOR, "[data-test-id='next-button']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "[name='password']")

    ENTER_BUTTON = (By.CSS_SELECTOR, "[data-test-id='submit-button']")


class MessagePageLocators:
    CHECK_EMAIL = (By.CSS_SELECTOR, ".ph-project__user-name")
    TRY_CALENDAR_ALERT = (By.CSS_SELECTOR,".ph-project-promo-close-icon__container")
    WRITE_MESSAGE_BUTTON = (By.CSS_SELECTOR, "span.compose-button__txt")

    RECEIVER_FIELD = (By.CSS_SELECTOR, ".container--hmD9c input.container--H9L5q")
    THEME_FIELD = (By.CSS_SELECTOR, ".subject__container--HWnat input.container--H9L5q")
    BODY_FIELD_TO_CLEAR = (By.CSS_SELECTOR, "[data-signature-widget='content'] div")
    BODY_FIELD = (By.XPATH, "//div[contains(@class,'cke_editable')]/div[1]")
    SEND_MESSAGE_BUTTON = (By.CSS_SELECTOR, "[data-test-id='send']")

    CLOSE_BUTTON = (By.CSS_SELECTOR, "[data-highlighted-class='button2_highlighted'].button2_close")

    TO_MYSELF_BUTTON = (By.CSS_SELECTOR, "[href='/tomyself/?']")
    THEME_IN_MESSAGE = (By.CSS_SELECTOR, "")
    BODY_IN_MESSAGE = (By.CSS_SELECTOR, "")

