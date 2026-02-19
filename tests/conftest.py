import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.attach import add_screenshot, add_page_source, add_console_logs, add_video


@pytest.fixture(scope='function')
def setup_browser():
    options = Options()

    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "128.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    yield driver

    add_screenshot(driver)
    add_page_source(driver)
    add_console_logs(driver)
    add_video(driver)

    driver.quit()