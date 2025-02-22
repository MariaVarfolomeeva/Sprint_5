import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

BASE_URL = "https://stellarburgers.site"
BURGER_URL = f"{BASE_URL}/burger"
ACCOUNT_URL = f"{BASE_URL}/account"
REGISTER_URL = f"{BASE_URL}/register"
RECOVERY_URL = f"{BASE_URL}/recovery"
LOGIN_URL = f"{BASE_URL}/login"

@pytest.fixture
def get_driver(browser='chrome'):
    """ Функция для получения WebDriver для выбранного браузера """
    if browser == 'chrome':
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser == 'firefox':
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    else:
        raise ValueError("Unsupported browser: choose either 'chrome' or 'firefox'")

    driver.maximize_window()
    yield driver
    driver.quit()
