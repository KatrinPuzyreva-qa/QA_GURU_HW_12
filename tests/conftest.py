import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from utils import attach


@pytest.fixture(scope='function')
def setup_browser():
    # Устанавливаем нужные опции браузера
    options = Options()
    options.headless = True  # Если нужен режим без графического интерфейса
    options.add_argument('--window-size=1920,1080')  # Размер окна браузера

    # Используем менеджер драйверов для автоматического выбора подходящей версии chrome
    service = webdriver.ChromeService(ChromeDriverManager().install())

    # Инициализация удалённого веб-драйвера
    driver = webdriver.Remote(
        command_executor="https://user1:1234@ru.selenoid.autotests.cloud/wd/hub",
        options=options,
        desired_capabilities={'browserName': 'chrome'}
    )


    yield driver
    #driver.quit()  # Завершаем работу браузера после окончания теста


    # Сохраняем скриншоты, логи браузера и видео после каждого теста
    attach.add_screenshot(driver)
    attach.add_console_logs(driver)
    attach.add_page_source(driver)
    attach.add_video(driver)

    driver.quit()


