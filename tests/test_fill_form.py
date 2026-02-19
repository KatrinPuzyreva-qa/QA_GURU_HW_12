import allure
from selenium import webdriver

from pages.registration_page import RegistrationPage

@allure.title("Successful fill form")
def test_fill_form():
    driver = webdriver.Chrome()
    registration_page = RegistrationPage(driver)

    with allure.step("Open registrations form"):
        registration_page.open()
    with allure.step("Fill form"):
        registration_page.fill_username('Таисия')
        registration_page.fill_password('12345678')
        registration_page.submit()
    with allure.step("Check form results"):
        registration_page.should_have_submission_confirmation()

