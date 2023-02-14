import pytest
from pages.locators import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

base_url = 'https://stellarburgers.nomoreparties.site/'


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get(base_url)
    yield driver
    driver.quit()
