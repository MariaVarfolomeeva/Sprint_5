import pytest
from utils.locators import *
from fixtures.driver import get_driver

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_logout(driver):
    driver.get("https://stellarburgers.site/account")

    driver.find_element(*LOGOUT_BUTTON).click()

    assert driver.current_url == "https://stellarburgers.site/"

    driver.quit()