from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators


class TestPersonalAccount:
    def test_go_to_personal_account(self, driver, registration):
        """Проверка перехода в личный кабинет после авторизации"""
        driver.get("https://stellarburgers.nomoreparties.site/login")

        email_field = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(locators.LoginPageLocators.EMAIL_INPUT)
        )
        email_field.send_keys(registration["email"])

        password_field = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(locators.LoginPageLocators.PASSWORD_INPUT)
        )
        password_field.send_keys(registration["password"])

        submit_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(locators.LoginPageLocators.LOGIN_BUTTON)
        )
        submit_button.click()

        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(locators.MainPage.MAKE_ORDER_BUTTON)
        )

        account_link = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(locators.AccountPageLocators.ACCOUNT_LINK)
        )
        account_link.click()

        WebDriverWait(driver, 15).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/account/profile"))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"


    def test_logout_from_personal_account(self, driver, registration):
        """Проверка выхода из аккаунта через личный кабинет"""
        driver.get("https://stellarburgers.nomoreparties.site/login")

        email_field = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(locators.LoginPageLocators.EMAIL_INPUT)
        )
        email_field.send_keys(registration["email"])

        password_field = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(locators.LoginPageLocators.PASSWORD_INPUT)
        )
        password_field.send_keys(registration["password"])

        submit_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(locators.LoginPageLocators.LOGIN_BUTTON)
        )
        submit_button.click()

        account_link = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(locators.AccountPageLocators.ACCOUNT_LINK)
        )
        account_link.click()

        logout_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(locators.AccountPageLocators.LOGOUT_BUTTON)
        )
        logout_button.click()

        WebDriverWait(driver, 15).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
