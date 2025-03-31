from selenium.webdriver.support import expected_conditions as EC
import locators
from generate_date import generate_email, generate_password


def test_successful_registration(driver, wait, registration):
    """Проверка успешной регистрации"""
    assert isinstance(registration["name"], str) and len(registration["name"]) > 0
    assert isinstance(registration["email"], str) and "@" in registration["email"]
    assert isinstance(registration["password"], str) and len(registration["password"]) >= 6

    wait.until(EC.url_contains("/login"))


def test_short_password_error(driver, wait):
    """Проверка ошибки при коротком пароле"""
    driver.get("https://stellarburgers.nomoreparties.site/register")

    test_data = {
        "name": "Kira",
        "email": generate_email(),
        "password": "12345"
    }

    wait.until(
        EC.visibility_of_element_located(locators.RegistrationLocators.NAME_FIELD)
    ).send_keys(test_data["name"])

    wait.until(
        EC.visibility_of_element_located(locators.RegistrationLocators.EMAIL_FIELD)
    ).send_keys(test_data["email"])

    password_field = wait.until(
        EC.visibility_of_element_located(locators.RegistrationLocators.PASSWORD_FIELD)
    )
    password_field.send_keys(test_data["password"])

    register_button = wait.until(
        EC.presence_of_element_located(locators.RegistrationLocators.REGISTER_BUTTON)
    )

    assert register_button.get_attribute("disabled") != "true"
    assert "register" in driver.current_url


def test_empty_password_error(driver, wait):
    """Проверка ошибки при пустом пароле"""
    driver.get("https://stellarburgers.nomoreparties.site/register")

    test_data = {
        "name": "Kira",
        "email": generate_email(),
        "password": ""
    }

    wait.until(
        EC.visibility_of_element_located(locators.RegistrationLocators.NAME_FIELD)
    ).send_keys(test_data["name"])

    wait.until(
        EC.visibility_of_element_located(locators.RegistrationLocators.EMAIL_FIELD)
    ).send_keys(test_data["email"])

    password_field = wait.until(
        EC.visibility_of_element_located(locators.RegistrationLocators.PASSWORD_FIELD)
    )
    password_field.send_keys(test_data["password"])

    register_button = wait.until(
        EC.presence_of_element_located(locators.RegistrationLocators.REGISTER_BUTTON)
    )

    assert register_button.get_attribute("disabled") != "true"
    assert "register" in driver.current_url
