from selenium import webdriver


def test_driver_run(tbase):
    browser = tbase.wd
    mPage = tbase.MainPage
    mPage.navigate()
    mPage.clickABTestingLnk()
    header = tbase.ABTesting.getHeader()
    assert header == 'A/B Test Control' 
    # don't know why it doesn't works from fixture, will use it from here for a while
    browser.quit()