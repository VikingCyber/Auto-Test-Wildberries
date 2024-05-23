from pages.main_page import MainPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


def test_search(driver):
    main_page = MainPage(driver)
    main_page.search_for_item("Браслет")
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(main_page.catalog))
    sleep(3)
    assert main_page.search_confirmation()
