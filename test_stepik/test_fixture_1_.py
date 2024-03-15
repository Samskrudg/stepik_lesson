import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_Links:
    @pytest.fixture(scope="function")
    def browser(self):
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        yield browser
        browser.quit()


    @pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1",
                                       "https://stepik.org/lesson/236896/step/1",
                                       "https://stepik.org/lesson/236897/step/1",
                                       "https://stepik.org/lesson/236898/step/1",
                                       "https://stepik.org/lesson/236899/step/1",
                                       "https://stepik.org/lesson/236903/step/1",
                                       "https://stepik.org/lesson/236904/step/1",
                                       "https://stepik.org/lesson/236905/step/1"])
    def test_login_link(self, browser, link,):
        browser.get(link)

        browser.implicitly_wait(5)
        entrance_button = browser.find_element(By.CLASS_NAME, 'ember-view.navbar__auth.navbar__auth_login.st-link.st-link_style_button')
        browser.implicitly_wait(5)
        entrance_button.click()

        login_button = browser.find_element(By.NAME, 'login')
        login_button.send_keys('введи свой логин')

        login_button = browser.find_element(By.NAME, 'password')
        login_button.send_keys('введи свой пароль')

        send_button = browser.find_element(By.CSS_SELECTOR, 'button.sign-form__btn.button_with-loader ')
        browser.implicitly_wait(5)
        send_button.click()

        time.sleep(5)

        try:
            time.sleep(5)
            browser.implicitly_wait(5)
            send_two_button = browser.find_element(By.CLASS_NAME, "ember-text-area.ember-view.textarea.string-quiz__textarea")
            browser.implicitly_wait(5)
            send_two_button.send_keys(str(self.answer()))
            browser.implicitly_wait(5)
            button = browser.find_element(By.CLASS_NAME, 'submit-submission')
            button.click()

        finally:
            time.sleep(30)
            browser.quit()

    def answer(self):
        import math
        return math.log(int(time.time() + 48))