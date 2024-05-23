from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.ID, 'searchInput')
        self.login_button = (By.XPATH, '//*[@id="basketContent"]/div[2]/a')
        self.catalog = (By.ID, 'catalog')

    def click_login(self):
        login_button = self.driver.find_element(*self.login_button)
        login_button.click()

    def search_for_item(self, item):
        search_input = self.driver.find_element(*self.search_box)
        search_input.clear()
        search_input.send_keys(item)
        search_input.send_keys(Keys.ENTER)


    def search_confirmation(self):
        try:
            self.driver.find_element(*self.catalog).is_displayed()
            return True
        except NoSuchElementException:
            return False


