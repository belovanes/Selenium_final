import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox. hchrome - for chrome in HEADLESS-mode")

    parser.addoption('--language', action='store', default='en',
                     help="Choose user language: ru | en| fr | etc...")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    print(f'\nUsing {browser_name} browser')
    print(f'User language {user_language}')
    browser = None

    if (browser_name == "chrome") or (browser_name == "hchrome"):
        print("Start chrome browser for test")
        options = webdriver.ChromeOptions()
        if browser_name == "hchrome":
            options.headless = True
            print("Using Headless mode")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])  # отключаем вывод дополнительной информации в лог
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        print("Start firefox browser for test")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)

    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    
    yield browser
    print("\nbrowser quit")
    browser.quit()
