import pytest
from selenium import webdriver
from time import sleep
from pages.sbis_ru import sbis_ru as Sbis_ru
from pages.sbis_ru_contact import sbis_contact as Sbis_ru_contact
from pages.tensor_ru import tensor_ru as Tensor_ru
from pages.tensor_ru_about_ import tensor_about_ru as Tensor_ru_about

browser = webdriver.Chrome()

def test_first_script():
    sbis_ru = Sbis_ru(browser)
    sbis_ru.open()
    sbis_ru.click_contact()

    sbis_ru_contact = Sbis_ru_contact(browser)
    sbis_ru_contact.click_tensor_banner()
    sbis_ru_contact.select_last_page()

    tensor_ru = Tensor_ru(browser)
    tensor_ru.click_block4_about()

    tensor_ru_about = Tensor_ru_about(browser)

    if not tensor_ru_about.checkUrl():
        assert False, tensor_ru_about.url + ' не открылся'

    error = tensor_ru_about.check_block_3_photo_same_size()
    assert not error, error

def test_second_script():
    user_region = 76
    new_region = 41

    sbis_ru = Sbis_ru(browser)
    sbis_ru.open()
    sbis_ru.click_contact()

    print(browser.current_url)

    sbis_ru_contact = Sbis_ru_contact(browser)
    old_city = sbis_ru_contact.get_city_id_2()

    if not sbis_ru_contact.check_current_region(user_region):
        assert False, 'Текущий регион отличается от ожидаемого'

    if not sbis_ru_contact.choise_region(new_region):
        assert False, 'Не удалось сменить регион'

    sleep(1)

    if not sbis_ru_contact.check_region_in_title(new_region):
        assert False, 'Название региона ненайдено в title'

    if not sbis_ru_contact.check_region_in_url(new_region):
        assert False, 'Название региона ненайдено в url'

    if old_city == sbis_ru_contact.get_city_id_2():
        assert False, 'Список партнёров не обновился'
    assert True
