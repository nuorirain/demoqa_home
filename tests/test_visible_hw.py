import time
from pages.accordion import Accordion
from selenium.common.exceptions import NoSuchElementException

def test_visible_accordion(driver):
    page = Accordion(driver)
    page.open()

    section1 = page.find_element(page.section1_content)
    assert section1.is_displayed(), "Элемент #section1Content > p не виден!"
    heading1 = page.find_element(page.section1_heading)
    heading1.click()

    time.sleep(2)
    try:
        section1 = page.find_element(page.section1_content)
        assert not section1.is_displayed(), "Элемент #section1Content > p всё ещё виден!"
    except NoSuchElementException:
        pass  

def test_visible_accordion_default(driver):
    page = Accordion(driver)
    page.open()

    elements = [
        page.section2_content_1,
        page.section2_content_2,
        page.section3_content
    ]

    for locator in elements:
        try:
            elem = page.find_element(locator)
            assert not elem.is_displayed(), f"❌ Элемент {locator} должен быть скрыт!"
        except NoSuchElementException:
            pass 
