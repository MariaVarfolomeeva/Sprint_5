import pytest
from utils.locators import *
from fixtures.conftest import LOGIN_URL, ACCOUNT_URL, REGISTER_URL, RECOVERY_URL


def test_login_from_main_page(driver):
    driver.get("https://stellarburgers.site/")
    driver.find_element(*LOGIN_BUTTON_MAIN).click()
    assert driver.current_url == LOGIN_URL


def test_login_from_personal_account_button(driver):
    driver.get("https://stellarburgers.site/")
    driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
    assert driver.current_url == ACCOUNT_URL


def test_login_from_registration_form(driver):
    driver.get(REGISTER_URL)
    driver.find_element(*LOGIN_FROM_REGISTRATION_BUTTON).click()
    assert driver.current_url == LOGIN_URL


def test_login_from_password_recovery_form(driver):
    driver.get(RECOVERY_URL)
    driver.find_element(*LOGIN_FROM_RECOVERY_BUTTON).click()
    assert driver.current_url == LOGIN_URL
