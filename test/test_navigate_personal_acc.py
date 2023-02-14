from conftest import base_url
from pages.locators import AppHeader, AuthorizationForm, wait_el, MainPage
from utils import email, password


class TestNavigateToPersonalAccount:
    def test_navigate_to_pesronal_account_true(self, driver):
        driver.get(base_url)
        driver.find_element(*AppHeader.link_acc).click()
        wait_el(driver, AuthorizationForm.title_login_page)
        driver.find_element(*AuthorizationForm.email).send_keys(email)
        driver.find_element(*AuthorizationForm.password).send_keys(password)
        driver.find_element(*AuthorizationForm.button_login).click()
        wait_el(driver, MainPage.title_main_page)
        driver.find_element(*AppHeader.link_acc).click()
        current_url = driver.current_url
        assert current_url == base_url + 'account'
