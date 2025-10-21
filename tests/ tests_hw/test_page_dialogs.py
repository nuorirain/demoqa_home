import time
from pages.modal_dialogs import ModalDialogs

def test_modal_elements(driver):
    page = ModalDialogs(driver)
    page.open()
    count = page.get_buttons_count()
    assert count == 5, f"❌ Ожидалось 5 кнопок, но найдено {count}"


def test_navigation_modal(driver):
    page = ModalDialogs(driver)
    page.open()

    driver.refresh()

    home_icon = page.find_element(page.icon_home)
    home_icon.click()
    driver.back()

    driver.set_window_size(900, 400)
    driver.forward()

    current_url = driver.current_url
    assert current_url == "https://demoqa.com/", f"❌ URL некорректен: {current_url}"


    title = driver.title
    assert "DEMOQA" in title.upper(), f"❌ Заголовок не содержит DEMOQA: {title}"

  
    driver.set_window_size(1000, 1000)
