from selenium.webdriver.chrome.webdriver import WebDriver
from base.pages.ab_testing_page import ABTesting
from base.pages.main_page import MainPage
import base.utils.json_reader as navigation

class Base:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.ABTesting = ABTesting(self.wd)
        self.MainPage = MainPage(self.wd)

    def navigate(self):
        mainUrl = navigation.getMainUrl()
        self.wd.get(mainUrl)

    def close_browser(self):
        self.wd.quit()
