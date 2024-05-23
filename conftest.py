import pytest
from selenium import webdriver


# Тут можно использовать session, но использую fucntion чтобы каждый тест был более явным
@pytest.fixture(scope='session', autouse=True)
def driver():
    options = webdriver.EdgeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Edge(options=options)
    driver.get(url='https://www.wildberries.ru/')
    yield driver
    driver.quit()
