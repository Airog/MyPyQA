from selenium.webdriver.chrome.webdriver import WebDriver
from base.pages.ab_testing_page import ABTesting
from base.pages.main_page import MainPage

class Base:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.ABTesting = ABTesting(self.wd)
        self.MainPage = MainPage(self.wd)

    def navigate(self, url):
        self.wd.get(url)

    def close_browser(self):
        self.wd.quit()
