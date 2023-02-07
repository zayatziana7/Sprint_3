import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from pages.locators import *
from utils import *




base_url = 'https://stellarburgers.nomoreparties.site/'

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(base_url)
    yield driver
    driver.quit()


