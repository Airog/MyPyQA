import base.utils.json_reader as navigation

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def mainUrl(self):
        return navigation.getMainUrl()

    def navigate(self):
        self.driver.get(self.mainUrl())