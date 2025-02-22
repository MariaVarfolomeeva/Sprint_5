import pytest
from utils.locators import *
from fixtures.conftest import BASE_URL, ACCOUNT_URL


def test_logout(driver):
    driver.get(ACCOUNT_URL)

    driver.find_element(*LOGOUT_BUTTON).click()

    assert driver.current_url == BASE_URL
