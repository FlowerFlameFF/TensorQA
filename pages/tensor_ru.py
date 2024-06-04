from selenium.webdriver.common.by import By
from pages.base_page import base_page

block4_selector = (By.CLASS_NAME, 'tensor_ru-Index__block4-content')
block4_about_selector = (By.CSS_SELECTOR, 'a[href="/about"]')

class tensor_ru(base_page):
    def __init__(self, browser):
        super().__init__(browser)
        self.url = 'https://tensor.ru'

    def click_block4_about(self):
        blocl4_about = self.find_element(block4_selector).find_element(*block4_about_selector)
        self.click(blocl4_about)
