from selenium import webdriver


def test_driver_run():
    browser = webdriver.Chrome()
    browser.get('http://the-internet.herokuapp.com/')
    ab_testing_el = browser.find_element_by_css_selector('#content ul li:nth-child(1) a')
    ab_testing_el.click()
    header = browser.find_element_by_css_selector('#content > div > h3').text
    assert header == 'A/B Test Control'
    browser.quit()