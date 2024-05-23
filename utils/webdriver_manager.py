# from selenium import webdriver
# from selenium.webdriver.edge.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
#
#
# class WebDriverManager:
#     def __init__(self, browser='edge'):
#         self.browser = browser.lower()
#
#     def get_driver(self):
#         if self.browser == 'edge':
#             service = Service(EdgeChromiumDriverManager().install())
#             options = webdriver.EdgeOptions()
#             options.add_argument('--start-maximized')
#             driver = webdriver.Edge(service=service, options=options)
#         elif self.browser == 'chrome':
#             service = Service(ChromeDriverManager().install())
#             options = webdriver.ChromeOptions()
#             options.add_argument('--start-maximized')
#             driver = webdriver.Chrome(service=service, options=options)
#         else:
#             raise ValueError(f"Не поддерживается автоматическая загрузка драйверов для вашего браузера. Информация:"
#                              f"https://developer.chrome.com/docs/chromedriver/get-started?hl=ru")
#         return driver
