from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
from selenium.webdriver.support.wait import WebDriverWait
from helper_tests import simple_assert, boolean_assert

driver = webdriver.Chrome()
main_url = ('https://www.malmomusikaffar.com/')
electric_guitars = ('https://www.malmomusikaffar.com/stranginstrument/gitarr/elgitarrer')
cart = ('https://www.malmomusikaffar.com/checkout/cart/')


# driver.get(main_url)

# SETUP & TEARDOWN
@pytest.fixture
def load_driver():

    driver = webdriver.Chrome()

    yield driver

    driver.quit()

# Test 1: Kontrollera att url:en stämmer
def test_1(load_driver):
    driver = load_driver
    driver.get(main_url)
    boolean_assert("malmomusikaffar" in driver.current_url, f"Expected malmomusikaffar in url, got: {driver.current_url}")


# Test 2: Kontrollera att det går att lägga till Eastman T59/V Antique Red i kundkorg
def test_2(load_driver):
    driver = load_driver

    # Hämta elgitarrsida
    driver.get(electric_guitars)

    # Identifiera rätt gitarr och klicka på länken
    find_guitar = driver.find_element(By.XPATH, '//*[@id="amasty-shopby-product-list"]/div[2]/ol/li[39]/div/div/header/a')
    driver.execute_script("arguments[0].click();", find_guitar)

    # Lägg till i kundkorg och vänta
    add_to_cart = driver.find_element(By.XPATH, '//*[@id="product-addtocart-button"]')
    driver.execute_script("arguments[0].click();", add_to_cart)
    time.sleep(5)

    # Gå till kundkorg och kontrollera att rätt produkt ligger där
    driver.get(cart)
    guitar_link = driver.find_element(By.LINK_TEXT, 'https://www.malmomusikaffar.com/eastman-t59-v-antique-red-16950271')
    boolean_assert("T59/V Antique Red" in guitar_link, f"Expected T59/V Antique Red, got: {guitar_link}")
    # T59/V Antique Red


# Test 3: Kontrollera att facebooklänken stämmer
def test_3(load_driver):
    driver = load_driver
    driver.get(main_url)
    facebook_link = driver.find_element(By.XPATH, '//*[@id="html-body"]/div[4]/footer/div[1]/div[2]/ul/li[1]/a')
    driver.execute_script("arguments[0].click();", facebook_link)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(5)
    boolean_assert("https://www.facebook.com/MalmoMusikaffar" in driver.current_url, f"Expected https://www.facebook.com/MalmoMusikaffar in url, got: {driver.current_url}")
    