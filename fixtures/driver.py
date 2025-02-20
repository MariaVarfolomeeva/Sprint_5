from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def get_driver(browser='chrome'):
    """ Функция для получения WebDriver для выбранного браузера """
    if browser == 'chrome':
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser == 'firefox':
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    else:
        raise ValueError("Unsupported browser: choose either 'chrome' or 'firefox'")

    driver.maximize_window()
    return driver