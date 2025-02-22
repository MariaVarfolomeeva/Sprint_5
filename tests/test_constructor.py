import pytest
from utils.locators import *
from fixtures.conftest import BURGER_URL


def test_transition_to_buns_section(driver):
    driver.get(BURGER_URL)
    driver.find_element(*BUNS_SECTION).click()
    assert "buns" in driver.current_url


def test_transition_to_sauces_section(driver):
    driver.get(BURGER_URL)
    driver.find_element(*SAUCES_SECTION).click()
    assert "sauces" in driver.current_url


def test_transition_to_fillings_section(driver):
    driver.get(BURGER_URL)
    driver.find_element(*FILLINGS_SECTION).click()
    assert "fillings" in driver.current_url
