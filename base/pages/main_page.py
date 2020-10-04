import base.utils.json_reader as navigation
from base.pages.base_page import BasePage

class MainPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def clickABTestingLnk(self):
        d = self.driver
        d.find_element_by_css_selector('#content > ul > li:nth-child(1) > a').click()