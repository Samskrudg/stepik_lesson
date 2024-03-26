import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='es',
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    # записали в переменную передаваемый язык
    user_language = request.config.getoption("language")
    # создали опцию
    options = Options()
    # добавили опцию с нужным нам языком
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    # передали эту опцию браузеру
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    yield browser
    browser.quit()