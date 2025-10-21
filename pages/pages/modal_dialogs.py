from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ModalDialogs(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = "https://demoqa.com/modal-dialogs"
        self.buttons = (By.CSS_SELECTOR, "div.left-pannel button, div.left-pannel li, .element-group")
        self.icon_home = (By.CSS_SELECTOR, "header a > img")

    def open(self):
        self.visit(self.base_url)

    def get_buttons_count(self):
        elements = self.driver.find_elements(*self.buttons)
        return len(elements)
