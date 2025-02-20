import pytest
from utils.locators import *
from fixtures.driver import get_driver


@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


def test_transition_to_personal_account(driver):
    driver.get("https://stellarburgers.site/")

    driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()

    assert driver.current_url == "https://stellarburgers.site/account"
    driver.quit()
