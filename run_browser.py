from selenium import webdriver


def test_driver_run():
    browser = webdriver.Chrome()
    browser.get('https:\\www.google.com')
    browser.quit()