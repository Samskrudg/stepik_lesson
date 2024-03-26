import time

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    time.sleep(30)
    assert browser.find_element(By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")