from selenium.webdriver.common.by import By
from pages.base_page import base_page

contact_locator = (By.CSS_SELECTOR, 'a[href="/contacts"]')

class sbis_ru(base_page):
    def __init__(self, browser):
        super().__init__(browser)
        self.url = 'https://sbis.ru/'

    def click_contact(self):
        contact = self.find_element(contact_locator)
        self.click(contact)