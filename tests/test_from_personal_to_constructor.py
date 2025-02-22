import pytest
from utils.locators import *
from fixtures.conftest import BASE_URL, ACCOUNT_URL


def test_transition_from_personal_account_to_constructor(driver):
    driver.get(BASE_URL)

    driver.find_element(*CONSTRUCTOR_BUTTON).click()

    assert driver.current_url == ACCOUNT_URL

