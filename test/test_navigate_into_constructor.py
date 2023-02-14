from conftest import base_url
from pages.locators import AppHeader, MainPage


class TestConstructor:
    def test_click_link_constructor_true(self, driver):
        driver.get(base_url + 'login')
        driver.find_element(*AppHeader.link_constructor).click()
        current_url = driver.current_url
        assert current_url == base_url

    def test_click_link_logo_true(self, driver):
        driver.get(base_url + 'login')
        driver.find_element(*AppHeader.logo).click()
        current_url = driver.current_url
        assert current_url == base_url

    def test_section_check_bread_true(self, driver):
        driver.get(base_url)
        driver.find_element(*MainPage.sauce_element).click()
        bread_element = driver.find_element(*MainPage.bread_element)
        bread_element.click()
        current_element = driver.find_element(*MainPage.active_section)
        assert bread_element.text == current_element.text

    def test_section_check_sauces_true(self, driver):
        driver.get(base_url)
        sauce_element = driver.find_element(*MainPage.sauce_element)
        sauce_element.click()
        current_element = driver.find_element(*MainPage.active_section)
        assert sauce_element.text == current_element.text

    def test_section_check_fillings_true(self, driver):
        driver.get(base_url)
        filling_element = driver.find_element(*MainPage.filling_element)
        filling_element.click()
        current_element = driver.find_element(*MainPage.active_section)
        assert filling_element.text == current_element.text
