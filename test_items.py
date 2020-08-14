import time
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
def test_add_items(browser):
    browser.get(link)
    time.sleep(30)
    button = browser.find_element_by_xpath("//button[@type='submit']")
    assert button