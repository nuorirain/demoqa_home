import pytest
from selenium.webdriver.common.by import By
from components.base_component import BaseComponent

# 1-й тест
def test_footer_text(driver):
    driver.get("https://demoqa.com/")
    footer = BaseComponent(driver, "footer")
    footer_text = footer.get_text()

    assert footer_text == "© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.", \
        f"Ожидали другой текст, получили: {footer_text}"


# 2-й тест
def test_center_text_on_elements_page(driver):
    driver.get("https://demoqa.com/")
  
    button = driver.find_element(By.CSS_SELECTOR, "div.card-body h5")
    button.click()

    assert driver.current_url == "https://demoqa.com/elements"

    center_text_component = BaseComponent(driver, "div.col-12.mt-4.col-md-6")
    text = center_text_component.get_text()

  
    assert text == "Please select an item from left to start practice.", \
        f"Ожидали другой текст, получили: {text}"
