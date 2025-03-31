from selenium.webdriver.common.by import By


class RegistrationLocators:
    NAME_FIELD = (By.XPATH, "//label[contains(@class, 'input__placeholder') and contains(text(), 'Имя')]/following::input[1]") # Поле "Имя"
    EMAIL_FIELD = (By.XPATH, "//label[contains(@class, 'input__placeholder') and contains(text(), 'Email')]/following::input[1]") # Поле "Email"
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password']") # Поле "Пароль"
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']") # Кнопка "Зарегистрироваться"
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']") # Ссылка "Войти" после неуспешной регистрации

class LoginPageLocators:
    MAIN_LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")
    ACCOUNT_LINK = (By.XPATH, "//a[contains(@href, '/account')]")
    LOGIN_LINK = (By.XPATH, "//a[contains(@class, 'AppHeader_header__link__3D_hX') and .//p[text()='Личный Кабинет']]")
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//*[text()='Войти' and not(name()='ya-tr-span')]")
    LOGIN_HEADER = (By.XPATH, "//h2[text()='Вход']")

class AccountPageLocators:
    ACCOUNT_LINK = (By.XPATH, "//header//a[contains(@href, 'account')]")
    PROFILE_HEADER = (By.XPATH, "//h2[text()='Профиль']")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")


class ConstructorLocators:
    CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']/..")
    LOGO_LINK = (By.XPATH, "/html/body/div[1]/div/header/nav/div/a")
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")

    # Tabs
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']/parent::div")
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/parent::div")
    TOPPINGS_TAB = (By.XPATH, "//span[text()='Начинки']/parent::div")

    # Sections
    BUNS_SECTION = (By.XPATH, "//h2[text()='Булки']")
    SAUCES_SECTION = (By.XPATH, "//h2[text()='Соусы']")
    TOPPINGS_SECTION = (By.XPATH, "//h2[text()='Начинки']")

    # Items
    BUNS_ITEMS = (
    By.XPATH, "//h2[text()='Булки']/following-sibling::ul//div[contains(@class, 'BurgerIngredient_ingredient__')]")
    SAUCES_ITEMS = (
    By.XPATH, "//h2[text()='Соусы']/following-sibling::ul//div[contains(@class, 'BurgerIngredient_ingredient__')]")
    TOPPINGS_ITEMS = (
    By.XPATH, "//h2[text()='Начинки']/following-sibling::ul//div[contains(@class, 'BurgerIngredient_ingredient__')]")
