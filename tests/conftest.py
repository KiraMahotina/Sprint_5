import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from generate_date import generate_email, generate_password
import locators


@pytest.fixture
def driver():
    """Фикстура для инициализации браузера"""
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture
def wait(driver):
    """Фикстура для явных ожиданий"""
    return WebDriverWait(driver, 15)


@pytest.fixture
def registration(driver):
    """Фикстура регистрации"""
    driver.get("https://stellarburgers.nomoreparties.site/register")

    email = generate_email()
    password = generate_password()
    name = "Kira"

    name_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(locators.RegistrationLocators.NAME_FIELD)
    )
    name_field.send_keys(name)

    email_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(locators.RegistrationLocators.EMAIL_FIELD)
    )
    email_field.send_keys(email)

    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(locators.RegistrationLocators.PASSWORD_FIELD)
    ).send_keys(password)

    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(locators.RegistrationLocators.REGISTER_BUTTON)
    ).click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("/login")
    )
    return {
        "email": email,
        "password": password,
        "name": name
    }

@pytest.fixture  #фикстура входа
def login_user(driver, registration):
    email = registration["email"]
    password = registration["password"]
    driver.get("https://stellarburgers.nomoreparties.site/login")  # перешли по ссылке
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div").send_keys(email)    #заполнили поле
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div").send_keys(password)    #заполнили поле
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button").click()   #нажали Войти
    WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))    #ожидаем перехода на главную страницу
    return {"email": email, "password": password}

@pytest.fixture  #фикстура выхода
def logout(driver):
    driver.get("https://stellarburgers.nomoreparties.site")  #перешли по ссылке
    driver.find_element(By.XPATH, "/html/body/div/div/header/nav/a/p").click()  #перешли в личный кабинет
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/nav/ul/li[3]/button").click()   # нажали выход
    WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))  #ожидаем главную страницу
