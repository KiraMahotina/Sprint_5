# 🍔 Тестирование сервиса Stellar Burgers

## 📋 О проекте
Автоматизированные тесты для веб-приложения конструктора бургеров [Stellar Burgers](https://stellarburgers.nomoreparties.site). Проект включает тестирование ключевых функциональных сценариев работы с сервисом.

## 🛠 Техническая реализация
Проект реализован с использованием:
- Python 3.9+
- Selenium WebDriver
- Pytest (тестовый фреймворк)
- Allure Framework (отчеты)

## 📂 Структура проекта

### Вспомогательные файлы:
1**`locators.py`** - локаторы элементов на страницах сайта

2**`conftest.py`** - фикстуры:
   - `driver` - инициализация браузера
   - `wait` - явные ожидания
   - `registration` - регистрация пользователя
3**`generate_data.py`** - генерация валидных тестовых данных

### Тестовые сценарии:

#### 1. Регистрация пользователя (`test_registration.py`)
- ✅ `test_successful_registration` - успешная регистрация
- ✅ `test_short_password_error` - ошибка при коротком пароле
- ✅ `test_empty_password_error` - ошибка при пустом пароле

#### 2. Авторизация (`test_login.py`)
- ✅ `test_login_from_main_button` - вход через кнопку "Войти в аккаунт"
- ✅ `test_login_from_personal_account` - вход через "Личный кабинет"
- ✅ `test_login_from_registration_page` - вход со страницы регистрации
- ✅ `test_login_from_password_recovery` - вход со страницы восстановления пароля

#### 3. Личный кабинет (`test_personal_account.py`)
- ✅ `test_go_to_personal_account` - переход в личный кабинет
- ✅ `test_logout_from_personal_account` - выход из аккаунта

#### 4. Конструктор (`test_constructor.py`)
- ✅ `test_go_to_constructor_from_account` - переход через кнопку "Конструктор"
- ✅ `test_go_to_constructor_from_logo` - переход через логотип
- ✅ `test_buns_section_default` - проверка раздела "Булки"
- ✅ `test_sauces_section_navigation` - проверка раздела "Соусы"
- ✅ `test_toppings_section_navigation` - проверка раздела "Начинки"
- ✅ `test_return_to_buns_section` - возврат в раздел "Булки"


