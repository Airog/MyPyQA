class ABTesting:
    def __init__(self, driver):
        self.driver = driver

    def getHeader(self):
        d = self.driver
        text = d.browser.find_element_by_css_selector('#content > div > h3').text
        return text