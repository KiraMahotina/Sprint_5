from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import locators


def test_go_to_constructor_from_account(driver, wait, registration):
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

    constructor_link = wait.until(EC.element_to_be_clickable(locators.ConstructorLocators.CONSTRUCTOR_LINK))
    constructor_link.click()

    wait.until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

    assemble_burger_text = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Соберите бургер')]"))
    )
    assert assemble_burger_text.is_displayed()

    order_button = wait.until(
        EC.visibility_of_element_located(locators.ConstructorLocators.ORDER_BUTTON)
    )
    assert order_button.is_displayed()


def test_go_to_constructor_from_logo(driver, wait, registration):
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
        EC.url_to_be("https://stellarburgers.nomoreparties.site/")
    )

    logo_link = wait.until(EC.element_to_be_clickable(locators.ConstructorLocators.LOGO_LINK))
    logo_link.click()

    wait.until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

    assemble_burger_text = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Соберите бургер')]"))
    )
    assert assemble_burger_text.is_displayed()

    order_button = wait.until(
        EC.visibility_of_element_located(locators.ConstructorLocators.ORDER_BUTTON)
    )
    assert order_button.is_displayed()


def test_buns_section_default(driver, wait):
    # Открываем главную страницу
    driver.get("https://stellarburgers.nomoreparties.site")
    wait.until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

    # 1 Проверяем, что по умолчанию выбран раздел "Булки"
    buns_tab = wait.until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'tab_tab')]//span[text()='Булки']"))
    )

    # Получаем родительский элемент вкладки
    tab_parent = buns_tab.find_element(By.XPATH, "./..")

    # Проверяем наличие класса, указывающего на активное состояние
    assert "tab_tab_type_current" in tab_parent.get_attribute("class")
    section = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//h2[contains(text(), 'Булки')]/following-sibling::ul")
        )
    )
    # Проверяем, что секция видима
    assert section.is_displayed()


def test_sauces_section_navigation(driver, wait):
    driver.get("https://stellarburgers.nomoreparties.site")
    # 2. Находим и кликаем вкладку "Соусы"
    sauces_tab = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'tab_tab')]//span[text()='Соусы']"))
    )
    sauces_tab.click()

    # Проверяем активность вкладки "Соусы"
    tab_parent = sauces_tab.find_element(By.XPATH, "./..")
    assert "tab_tab_type_current" in tab_parent.get_attribute("class")

    section = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//h2[contains(text(), 'Соусы')]/following-sibling::ul")
        )
    )
    # Проверяем, что секция видима
    assert section.is_displayed()


def test_toppings_section_navigation(driver, wait):
    driver.get("https://stellarburgers.nomoreparties.site")
    # 3 Находим и кликаем вкладку "Начинки"
    toppings_tab = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'tab_tab')]//span[text()='Начинки']"))
    )
    driver.execute_script("arguments[0].scrollIntoView();", toppings_tab)
    toppings_tab.click()

    # Проверяем активность вкладки "Начинки"
    tab_parent = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]//span[text()='Начинки']/.."))
    )

    section = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//h2[contains(text(), 'Начинки')]/following-sibling::ul")
        )
    )
    # Проверяем, что секция видима
    assert section.is_displayed()


def test_return_to_buns_section(driver, wait):
    driver.get("https://stellarburgers.nomoreparties.site")
    # 4 Заново переходим в Булки
    buns_tab = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'tab_tab')]//span[text()='Булки']")))

    driver.execute_script("arguments[0].scrollIntoView(true);", buns_tab)
    driver.execute_script("arguments[0].click();", buns_tab)

    # Проверяем активность вкладки
    tab_parent = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]//span[text()='Булки']/.."))
    )
    # Проверяем секцию
    section = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//h2[text()='Булки']/following-sibling::ul"))
    )
    assert section.is_displayed()
