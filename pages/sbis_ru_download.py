import re
import time
from selenium.webdriver.common.by import By
from pages.base_page import base_page

controls_tab_plugin_selector = (By.CSS_SELECTOR, 'div[data-id="plugin"]')
web_setup_plugin_download_link = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/a')
class sbis_ru_download(base_page):
    def __init__(self, browser):
        super().__init__(browser)
        self.url = 'https://sbis.ru/download'

    def choice_sbisplugin(self):
        controls_tab_plugin = self.find_element(controls_tab_plugin_selector)
        time.sleep(1)
        self.click(controls_tab_plugin)

    def get_web_setup_plugin_url(self):
        link = self.find_element(web_setup_plugin_download_link)
        url = link.get_attribute('href')
        return url

    def get_size_sbisplugin(self):
        self.wait()
        link = self.find_element(web_setup_plugin_download_link)
        text = link.text
        size = float(re.findall("\d+\.\d+", text)[0])
        return size