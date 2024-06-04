from selenium.webdriver.common.by import By
from pages.base_page import base_page

block3_images_selector = (By.CLASS_NAME, 'tensor_ru-About__block3-image')

class tensor_about_ru(base_page):
    def __init__(self, browser):
        super().__init__(browser)
        self.url = 'https://tensor.ru/about'

    def check_block_3_photo_same_size(self):
        images = self.find_elements(block3_images_selector)
        reference_size = images[0].size
        size_errors = ''

        for image in images[1:]:
            if reference_size != image.size:
                size_errors += 'Изображение "' + image.get_attribute('alt') + '" не подходит по размеру ' + str(image.size) + '\n'
        return size_errors