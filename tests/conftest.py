import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import attach


@pytest.fixture(scope='function')
def setup_browser():
    options = Options()

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )


    yield driver

    # Сохраняем скриншоты, логи браузера и видео после каждого теста
    attach.add_screenshot(driver)
    attach.add_console_logs(driver)
    attach.add_page_source(driver)
    attach.add_video(driver)

    driver.quit()


