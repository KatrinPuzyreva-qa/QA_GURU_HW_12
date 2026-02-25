import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from utils import attach


@pytest.fixture(scope='function')
def setup_browser():
    # Опции браузера
    options = Options()
    options.headless = True  # Без отображения графического интерфейса
    options.add_argument('--window-size=1920,1080')  # Окно размером 1920×1080 пикселей

    # Теперь используем сервис менеджера драйверов для автозапуска нужного драйвера

    service = webdriver.ChromeService(ChromeDriverManager().install())

    # Удалённое подключение к Selenoid
    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    # Драйвер возвращается и очищается после завершения теста
    yield driver
    driver.quit()



    # Сохраняем скриншоты, логи браузера и видео после каждого теста
    attach.add_screenshot(driver)
    attach.add_console_logs(driver)
    attach.add_page_source(driver)
    attach.add_video(driver)

    driver.quit()


