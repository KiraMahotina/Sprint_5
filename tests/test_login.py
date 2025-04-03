from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators


class TestLoginFunctionality:
    def test_login_from_main_button(self, driver, registration):
        """Вход через кнопку 'Войти в аккаунт' на главной"""
        driver.get("https://stellarburgers.nomoreparties.site")

        login_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(locators.LoginPageLocators.MAIN_LOGIN_BUTTON)
        )
        login_button.click()

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
            EC.url_matches("https://stellarburgers.nomoreparties.site/")
        )

        order_button = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(locators.MainPage.MAKE_ORDER_BUTTON))
        assert order_button.is_displayed()

    def test_login_from_personal_account(self, driver, registration):
        """Вход через кнопку 'Личный кабинет"""
        driver.get("https://stellarburgers.nomoreparties.site")

        account_link = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(locators.LoginPageLocators.ACCOUNT_LINK)
        )
        account_link.click()

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
            EC.url_matches("https://stellarburgers.nomoreparties.site/")
        )

        order_button = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(locators.MainPage.MAKE_ORDER_BUTTON))
        assert order_button.is_displayed()

    def test_login_from_registration_page(self, driver, registration):
        """Вход со страницы регистрации"""
        driver.get("https://stellarburgers.nomoreparties.site/register")

        account_link = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(locators.LoginPageLocators.LOGIN_BUTTON))
        account_link.click()

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
            EC.url_matches("https://stellarburgers.nomoreparties.site/")
        )

        order_button = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(locators.MainPage.MAKE_ORDER_BUTTON))
        assert order_button.is_displayed()

    def test_login_from_password_recovery(self, driver, registration):
        """Вход со страницы восстановления пароля"""
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

        account_link = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(locators.LoginPageLocators.LOGIN_LINK))
        account_link.click()

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
            EC.url_matches("https://stellarburgers.nomoreparties.site/")
        )

        order_button = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(locators.MainPage.MAKE_ORDER_BUTTON))
        assert order_button.is_displayed()