import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.main_page import MainPage
from pages.registration_page import RegistrationPage
from selenium.webdriver.support import expected_conditions as EC



def test_registration_positive(driver):
    main_page = MainPage(driver)
    registration_page = RegistrationPage(driver)
    main_page.click_login()
    driver.implicitly_wait(2)
    registration_page.enter_phone_number('79835754244')
    registration_page.submit_phone_number()
    time.sleep(2)
    assert registration_page.registration_confirmation()


def test_registration_negative(driver):
    main_page = MainPage(driver)
    registration_page = RegistrationPage(driver)
    main_page.click_login()
    driver.implicitly_wait(5)
    registration_page.enter_phone_number('333')
    registration_page.submit_phone_number()
    time.sleep(2)
    assert registration_page.registration_fail_confirmation()
