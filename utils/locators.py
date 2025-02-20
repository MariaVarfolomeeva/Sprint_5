from selenium.webdriver.common.by import By

REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
NAME_FIELD = (By.NAME, "name")
EMAIL_FIELD = (By.NAME, "email")
PASSWORD_FIELD = (By.NAME, "password")
ERROR_PASSWORD = (By.XPATH, "//div[contains(text(), 'Пароль слишком короткий')]")

LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
LOGIN_EMAIL = (By.NAME, "email")
LOGIN_PASSWORD = (By.NAME, "password")
FORGOT_PASSWORD_BUTTON = (By.XPATH, "//a[text()='Забыли пароль?']")
RESET_PASSWORD_EMAIL = (By.NAME, "reset-email")
RESET_PASSWORD_BUTTON = (By.XPATH, "//button[text()='Отправить']")

PROFILE_BUTTON = (By.XPATH, "//button[text()='Личный кабинет']")
LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выйти']")
CONSTRUCTOR_BUTTON = (By.XPATH, "//a[text()='Конструктор']")

BUNS_SECTION = (By.XPATH, "//a[text()='Булки']")
SAUCES_SECTION = (By.XPATH, "//a[text()='Соусы']")
FILLINGS_SECTION = (By.XPATH, "//a[text()='Начинки']")

REGISTER_SUCCESS_MESSAGE = (By.XPATH, "//div[contains(text(), 'Вы успешно зарегистрированы')]")