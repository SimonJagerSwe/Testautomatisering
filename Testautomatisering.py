from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait



driver = webdriver.Chrome()  # Optional argument, if not specified will search path.

driver.get('http://www.google.com/')