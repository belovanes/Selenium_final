import pytest
from selenium import webdriver

def myprint(st):
    print(f'\n\t\t--------+ {st} +--------\n')  # вывод контрольных точек

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox. hchrome - for chrome in HEADLESS-mode")

    parser.addoption('--language', action='store', default='en',
                     help="Choose user language: ru | en| fr | etc...")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    myprint(f'Using {browser_name} browser')
    myprint(f'User language {user_language}')
    browser = None

    if (browser_name == "chrome") or (browser_name == "hchrome"):
        myprint("start chrome browser for test")
        options = webdriver.ChromeOptions()
        if browser_name == "hchrome":
            options.headless = True
            myprint("Using Headless mode")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])  # отключаем вывод дополнительной информации в лог
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        myprint("start firefox browser for test")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)

    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    
    yield browser
    myprint("browser quit")
    browser.quit()