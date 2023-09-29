from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from helper_tests import simple_assert, boolean_assert

driver = webdriver.Chrome()
main_url = ('https://www.malmomusikaffar.com/')
electric_guitars = ('https://www.malmomusikaffar.com/stranginstrument/gitarr/elgitarrer')


driver.get(main_url)

# SETUP & TEARDOWN
@pytest.fixture
def load_driver():

    driver = webdriver.Chrome()

    yield driver

    driver.quit()

# Kontrollera att url:en stämmer
def test_1(load_driver):
    driver = load_driver
    driver.get(main_url)
    boolean_assert("malmomusikaffar" in driver.current_url, f"Expected malmomusikaffar in url, got: {driver.current_url}")


def test_2(load driver):
    driver = load_driver
    driver.get(electric_guitars)
    