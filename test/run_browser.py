from selenium import webdriver


def test_driver_run(tbase):
    # browser = webdriver.Chrome()
    # browser.get('http://the-internet.herokuapp.com/')

    browser = tbase.wd
    tbase.navigate('http://the-internet.herokuapp.com/')
    tbase.MainPage.clickABTestingLnk()
    header = tbase.ABTesting.getHeader()
    assert header == 'A/B Test Control' 
    # don't know why it doesn't works from fixture, will use it from here for a while
    browser.quit()