from conftest import base_url
from pages.locators import AuthorizationForm, MainPage, wait_el, AppHeader
from utils import email, password


class TestLogin:
    def test_authorization_main_page_true(self, driver):
        driver.get(base_url)
        driver.find_element(*MainPage.button_login_acc).click()
        driver.find_element(*AuthorizationForm.email).send_keys(email)
        driver.find_element(*AuthorizationForm.password).send_keys(password)
        driver.find_element(*AuthorizationForm.button_login).click()
        wait_el(driver, MainPage.title_main_page)
        checkout_button = driver.find_element(*MainPage.button_checkout).text
        assert checkout_button == 'Оформить заказ'

    def test_authorization_personal_account_true(self, driver):
        driver.get(base_url)
        driver.find_element(*AppHeader.link_acc).click()
        driver.find_element(*AuthorizationForm.email).send_keys(email)
        driver.find_element(*AuthorizationForm.password).send_keys(password)
        driver.find_element(*AuthorizationForm.button_login).click()
        wait_el(driver, MainPage.title_main_page)
        checkout_button = driver.find_element(*MainPage.button_checkout).text
        assert checkout_button == 'Оформить заказ'

    def test_authorization_button_registration_form_true(self, driver):
        driver.get(base_url + 'register')
        driver.find_element(*AuthorizationForm.button_login_reg_form).click()
        driver.find_element(*AuthorizationForm.email).send_keys(email)
        driver.find_element(*AuthorizationForm.password).send_keys(password)
        driver.find_element(*AuthorizationForm.button_login).click()
        wait_el(driver, MainPage.title_main_page)
        checkout_button = driver.find_element(*MainPage.button_checkout).text
        assert checkout_button == 'Оформить заказ'

    def test_authorization_by_the_password_setting_button_true(self, driver):
        driver.get(base_url + 'login')
        driver.find_element(*AuthorizationForm.button_password_setting).click()
        driver.find_element(*AuthorizationForm.button_login_reg_form).click()
        driver.find_element(*AuthorizationForm.email).send_keys(email)
        driver.find_element(*AuthorizationForm.password).send_keys(password)
        driver.find_element(*AuthorizationForm.button_login).click()
        wait_el(driver, MainPage.title_main_page)
        checkout_button = driver.find_element(*MainPage.button_checkout).text
        assert checkout_button == 'Оформить заказ'
