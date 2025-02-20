import pytest
from utils.locators import *
from fixtures.driver import get_driver, close_driver

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_successful_registration(driver):
    driver.get("https://stellarburgers.site/register")

    driver.find_element(*NAME_FIELD).send_keys("Test Testov")
    driver.find_element(*EMAIL_FIELD).send_keys("testtestov1999@yandex.ru")
    driver.find_element(*PASSWORD_FIELD).send_keys("password123")

    driver.find_element(*REGISTER_BUTTON).click()

    assert driver.find_element(*REGISTER_SUCCESS_MESSAGE)

    driver.quit()

def test_registration_with_invalid_password(driver):
    driver.get("https://stellarburgers.site/register")

    driver.find_element(*NAME_FIELD).send_keys("Test Testov")
    driver.find_element(*EMAIL_FIELD).send_keys("testtestov1999@yandex.ru")
    driver.find_element(*PASSWORD_FIELD).send_keys("123")

    driver.find_element(*REGISTER_BUTTON).click()

    error_message = driver.find_element(*PASSWORD_ERROR_MESSAGE).text
    assert "Пароль слишком короткий" in error_message

    driver.quit()