from selenium.webdriver.support import expected_conditions as EC
import locators

def test_go_to_personal_account(driver, wait, registration):
    """Проверка перехода в личный кабинет после авторизации"""
    driver.get("https://stellarburgers.nomoreparties.site/login")

    email_field = wait.until(
        EC.visibility_of_element_located(locators.LoginPageLocators.EMAIL_INPUT)
    )
    email_field.send_keys(registration["email"])

    password_field = wait.until(
        EC.visibility_of_element_located(locators.LoginPageLocators.PASSWORD_INPUT)
    )
    password_field.send_keys(registration["password"])

    submit_button = wait.until(
        EC.element_to_be_clickable(locators.LoginPageLocators.LOGIN_BUTTON)
    )
    submit_button.click()


    account_link = wait.until(
        EC.element_to_be_clickable(locators.AccountPageLocators.ACCOUNT_LINK)
    )
    account_link.click()

    wait.until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/account/profile"))


def test_logout_from_personal_account(driver, wait, registration):
    """Проверка выхода из аккаунта через личный кабинет"""
    driver.get("https://stellarburgers.nomoreparties.site/login")

    email_field = wait.until(
        EC.visibility_of_element_located(locators.LoginPageLocators.EMAIL_INPUT)
    )
    email_field.send_keys(registration["email"])

    password_field = wait.until(
        EC.visibility_of_element_located(locators.LoginPageLocators.PASSWORD_INPUT)
    )
    password_field.send_keys(registration["password"])

    submit_button = wait.until(
        EC.element_to_be_clickable(locators.LoginPageLocators.LOGIN_BUTTON)
    )
    submit_button.click()

    account_link = wait.until(
        EC.element_to_be_clickable(locators.AccountPageLocators.ACCOUNT_LINK)
    )
    account_link.click()

    logout_button = wait.until(
        EC.element_to_be_clickable(locators.AccountPageLocators.LOGOUT_BUTTON)
    )
    logout_button.click()

    wait.until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
