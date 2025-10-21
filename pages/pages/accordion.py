from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class Accordion(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = "https://demoqa.com/accordian"

        self.section1_heading = (By.ID, "section1Heading")
        self.section2_heading = (By.ID, "section2Heading")
        self.section3_heading = (By.ID, "section3Heading")

        self.section1_content = (By.CSS_SELECTOR, "#section1Content > p")
        self.section2_content_1 = (By.CSS_SELECTOR, "#section2Content > p:nth-child(1)")
        self.section2_content_2 = (By.CSS_SELECTOR, "#section2Content > p:nth-child(2)")
        self.section3_content = (By.CSS_SELECTOR, "#section3Content > p")

    def open(self):
        self.visit(self.base_url)
