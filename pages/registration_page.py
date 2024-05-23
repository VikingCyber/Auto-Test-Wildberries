from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.phone_input = (By.XPATH, '//*[@id="spaAuthForm"]/div/div[1]/div/div[2]/input')
        self.submit_button = (By.ID, 'requestCode')
        self.profile_list = (By.XPATH, '//*[@id="spaAuthForm"]/div/div[3]/div/img')
        self.error_msg = (By.XPATH, '//*[@id="spaAuthForm"]/div/div[2]/span[1]')

    def enter_phone_number(self, phone_number):
        phone_input = self.driver.find_element(*self.phone_input)
        phone_input.clear()
        phone_input.send_keys(phone_number)

    def submit_phone_number(self):
        submit_button = self.driver.find_element(*self.submit_button)
        submit_button.click()

    def registration_confirmation(self):
        try:
            self.driver.find_element(*self.profile_list).is_displayed()
            return True
        except NoSuchElementException:
            return False

    def registration_fail_confirmation(self):
        try:
            self.driver.find_element(*self.error_msg)
            return True
        except NoSuchElementException:
            return False
