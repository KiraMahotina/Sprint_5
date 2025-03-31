from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import locators


def test_login_from_main_button(driver, wait, registration):
    """Вход через кнопку 'Войти в аккаунт' на главной"""
    driver.get("https://stellarburgers.nomoreparties.site")

    login_button = wait.until(
        EC.element_to_be_clickable(locators.LoginPageLocators.MAIN_LOGIN_BUTTON)
    )
    login_button.click()

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

    wait.until(
        EC.url_matches("https://stellarburgers.nomoreparties.site/")
    )

    wait.until(
        EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Оформить заказ')]"))
    )


def test_login_from_personal_account(driver, wait, registration):
    """Вход через кнопку 'Личный кабинет"""
    driver.get("https://stellarburgers.nomoreparties.site")

    account_link = wait.until(
        EC.element_to_be_clickable(locators.LoginPageLocators.ACCOUNT_LINK)
    )
    account_link.click()

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

    wait.until(
        EC.url_matches("https://stellarburgers.nomoreparties.site/")
    )

    wait.until(
        EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Оформить заказ')]"))
    )


def test_login_from_registration_page(driver, wait, registration):
    """Вход со страницы регистрации"""
    driver.get("https://stellarburgers.nomoreparties.site/register")

    account_link = wait.until(EC.element_to_be_clickable(locators.LoginPageLocators.LOGIN_BUTTON))
    account_link.click()

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

    wait.until(
        EC.url_matches("https://stellarburgers.nomoreparties.site/")
    )

    wait.until(
        EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Оформить заказ')]"))
    )


def test_login_from_password_recovery(driver, wait, registration):
    """Вход со страницы восстановления пароля"""
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

    account_link = wait.until(EC.element_to_be_clickable(locators.LoginPageLocators.LOGIN_LINK))
    account_link.click()

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

    wait.until(
        EC.url_matches("https://stellarburgers.nomoreparties.site/")
    )

    wait.until(
        EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Оформить заказ')]"))
    )
