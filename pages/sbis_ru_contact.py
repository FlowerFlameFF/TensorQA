from selenium.webdriver.common.by import By
from pages.base_page import base_page

tensor_banner_locator = (By.CLASS_NAME, 'sbisru-Contacts__logo-tensor')
region_chooser_text_locator = (By.CLASS_NAME, 'sbis_ru-Region-Chooser__text')
city_id_2_locator = (By.ID, 'city-id-2')

region_dictionary = {
    76:{'full_title': 'Ярославская область',
        'short_title': 'Ярославская обл.',
        'translate_title': 'yaroslavskaya-oblast'
    },
    41:{'full_title': 'Камчатский Край',
        'short_title': 'Камчатский край',
        'translate_title': 'kamchatskij-kraj'
    }
}

class sbis_contact(base_page):
    def __init__(self, browser):
        super().__init__(browser)
        self.url = 'https://sbis.ru/contacts'

    def click_tensor_banner(self):
        tensor_banner = self.find_element(tensor_banner_locator)
        self.click(tensor_banner)

    def check_current_region(self, region_id):
        region_title = region_dictionary[region_id]['short_title']
        region_chooser_text = self.find_element(region_chooser_text_locator)
        return region_chooser_text.text == region_title

    def check_region_in_title(self, region_id):
        try:
            region_title = region_dictionary[region_id]['full_title']
            print(self.browser.title.title())
            print(self.browser.title.title().index(region_title))
            self.browser.title.title().index(region_title)
            return True
        except:
            return False

    def check_region_in_url(self, region_id):
        try:
            region_title = region_dictionary[region_id]['translate_title']
            print(self.browser.current_url)
            self.browser.current_url.index(region_title)

            return True
        except:
            return False

    def get_city_id_2(self):
        city_id_2 = self.find_element(city_id_2_locator)
        return city_id_2.text

    def choise_region(self, region_id):
        try:
            region_title = region_dictionary[region_id]['short_title']
            region_chooser_text = self.find_element(region_chooser_text_locator)
            self.click(region_chooser_text)
            self.wait()
            region_panel_item = self.find_element((By.CSS_SELECTOR, f'span[title="{region_title}"]'))
            self.click(region_panel_item)
            return True
        except:
            return False