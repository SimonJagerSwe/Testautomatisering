from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from helper_tests import simple_assert, boolean_assert

driver = webdriver.Chrome()
main_url = ('https://www.malmomusikaffar.com/')
electric_guitars = "https://www.malmomusikaffar.com/stranginstrument/gitarr/elgitarrer"


driver.get(main_url)

# SETUP & TEARDOWN
@pytest.fixture
def load_driver():

    driver = webdriver.Chrome()

    yield driver

    driver.quit()


def test_1(load_driver):
    driver.get(electric_guitars)
    driver.find_element_by_xpath('//*[@id="amasty-shopby-product-list"]/div[2]/ol/li[39]/div/div/header/strong/a')