import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='session')
def browser():
    """Фикстура для запуска браузера"""
    chrome_options = Options()
    chrome_options.add_argument('--disable-infobars')     # отключаем всплывающие уведомления
    chrome_options.add_argument('--disable-notifications')  # отключаем push-уведомления

    capabilities = {
        "browserName": "chrome",
        "browserVersion": "128.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    chrome_options.capabilities.update(capabilities)

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=chrome_options
    )

    yield driver

    driver.quit()


