from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators


class TestConstructorNavigation:
    def test_go_to_constructor_from_account(self, driver, registration):
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

        constructor_link = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(locators.ConstructorLocators.CONSTRUCTOR_LINK))
        constructor_link.click()

        WebDriverWait(driver, 15).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

        assemble_burger_text = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(locators.ConstructorLocators.BURGER_TEXT)
        )
        assert assemble_burger_text.is_displayed()

        order_button = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(locators.ConstructorLocators.ORDER_BUTTON)
        )
        assert order_button.is_displayed()


    def test_go_to_constructor_from_logo(self, driver, registration):
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
            EC.url_to_be("https://stellarburgers.nomoreparties.site/")
        )

        logo_link = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(locators.ConstructorLocators.LOGO_LINK))
        logo_link.click()

        WebDriverWait(driver, 15).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

        assemble_burger_text = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(locators.ConstructorLocators.BURGER_TEXT)
        )
        assert assemble_burger_text.is_displayed()

        order_button = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(locators.ConstructorLocators.ORDER_BUTTON)
        )
        assert order_button.is_displayed()


class TestIngredientSections:
    def test_buns_section_default(self, driver):
        # Открываем главную страницу
        driver.get("https://stellarburgers.nomoreparties.site")
        WebDriverWait(driver, 15).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

        # Проверяем активную вкладку
        active_tab = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(locators.ConstructorLocators.BUNS_ACTIV)
        )
        assert active_tab.is_displayed()

        buns_section = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(locators.ConstructorLocators.BUNS_SECTION)
        )
        assert buns_section.is_displayed()


    def test_sauces_section_navigation(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        # 2. Находим и кликаем вкладку "Соусы"
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(locators.ConstructorLocators.SAUCES_TAB)
        ).click()

        # Проверяем активную вкладку
        active_tab = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(locators.ConstructorLocators.SAUCES_ACTIV
            )
        )
        assert active_tab.is_displayed()

        # Проверяем видимость секции
        sauces_section = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(locators.ConstructorLocators.SAUCES_SECTION)
        )
        assert sauces_section.is_displayed()


    def test_toppings_section_navigation(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        # 3 Находим и кликаем вкладку "Начинки"
        toppings_tab = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(locators.ConstructorLocators.TOPPINGS_TAB)
        )
        driver.execute_script("arguments[0].scrollIntoView();", toppings_tab)
        toppings_tab.click()

        # Проверяем активность вкладки "Начинки"
        tab_parent = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(
                locators.ConstructorLocators.TOPPINGS_SECTION)
        )

        section = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(
                locators.ConstructorLocators.TOPPINGS_SECTION
            )
        )
        # Проверяем, что секция видима
        assert section.is_displayed()


    def test_return_to_buns_section(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        # 4 Заново переходим в Булки
        buns_tab = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(locators.ConstructorLocators.BUNS_TAB))

        driver.execute_script("arguments[0].scrollIntoView(true);", buns_tab)
        driver.execute_script("arguments[0].click();", buns_tab)

        # Проверяем активность вкладки
        tab_parent = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(
                locators.ConstructorLocators.BUNS_SECTION)
        )
        # Проверяем секцию
        section = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(locators.ConstructorLocators.BUNS_SECTION)
        )
        assert section.is_displayed()
