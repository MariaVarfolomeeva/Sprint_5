import pytest
from utils.locators import *
from fixtures.conftest import BASE_URL, ACCOUNT_URL


def test_transition_to_personal_account(driver):
    driver.get(BASE_URL)

    driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()

    assert driver.current_url == ACCOUNT_URL

