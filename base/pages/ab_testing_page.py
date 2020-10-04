import base.utils.json_reader as navigation
from base.pages.base_page import BasePage

class ABTesting(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def navigate(self):
        self.driver.get(super.mainUrl() + '/abtest')

    def getHeader(self):
        d = self.driver
        text = d.find_element_by_css_selector('#content > div > h3').text
        return text