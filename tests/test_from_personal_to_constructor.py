import pytest
from utils.locators import *
from fixtures.driver import get_driver


@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_transition_from_personal_account_to_constructor(driver):
    driver.get("https://stellarburgers.site/account")

    driver.find_element(*CONSTRUCTOR_BUTTON).click()

    assert driver.current_url == "https://stellarburgers.site/burger"

    driver.quit()