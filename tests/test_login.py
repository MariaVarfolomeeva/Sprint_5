import pytest
from utils.locators import *
from fixtures.driver import get_driver


@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


def test_login_from_main_page(driver):
    driver.get("https://stellarburgers.site/")
    driver.find_element(*LOGIN_BUTTON_MAIN).click()
    assert driver.current_url == "https://stellarburgers.site/login"
    driver.quit()


def test_login_from_personal_account_button(driver):
    driver.get("https://stellarburgers.site/")
    driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
    assert driver.current_url == "https://stellarburgers.site/account"
    driver.quit()


def test_login_from_registration_form(driver):
    driver.get("https://stellarburgers.site/register")
    driver.find_element(*LOGIN_FROM_REGISTRATION_BUTTON).click()
    assert driver.current_url == "https://stellarburgers.site/login"
    driver.quit()


def test_login_from_password_recovery_form(driver):
    driver.get("https://stellarburgers.site/recovery")
    driver.find_element(*LOGIN_FROM_RECOVERY_BUTTON).click()
    assert driver.current_url == "https://stellarburgers.site/login"
    driver.quit()
