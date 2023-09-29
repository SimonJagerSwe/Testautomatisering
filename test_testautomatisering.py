from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
from selenium.webdriver.support.wait import WebDriverWait
from helper_tests import simple_assert, boolean_assert

driver = webdriver.Chrome()
main_url = ('https://www.malmomusikaffar.com/')
electric_guitars = ('https://www.malmomusikaffar.com/stranginstrument/gitarr/elgitarrer')


# driver.get(main_url)

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


# Kontrollera att det går att lägga till Eastman T59/V Antique Red i kundkorg
def test_2(load_driver):
    driver = load_driver

    # Hämta elgitarrsida
    driver.get(electric_guitars)

    # Identifiera rätt gitarr och klicka på länken
    find_guitar = driver.find_element(By.XPATH, '//*[@id="amasty-shopby-product-list"]/div[2]/ol/li[39]/div/div/header/a')
    driver.execute_script("arguments[0].click();", find_guitar)

    # Lägg till i kundkorg
    add_to_cart = driver.find_element(By.XPATH, '//*[@id="product-addtocart-button"]')
    driver.execute_script("arguments[0].click();", add_to_cart)

    # Gå till kundkorg och kontrollera att rätt produkt ligger där
    in_cart = driver.find_element(By.XPATH, '//*[@id="html-body"]/div[4]/header/div[2]/div[1]/a')
    driver.execute_script("arguments[0].click();", in_cart)

# Kontrollera att facebooklänken stämmer
def test_3(load_driver):
    driver = load_driver
    driver.get(main_url)
    