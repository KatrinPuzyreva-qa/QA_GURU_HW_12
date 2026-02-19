import allure
from selene import browser, be
from selene.support.conditions import have


class RegistrationPage:
    def __init__(self):
        pass

    @allure.step("Open url https://the-internet.herokuapp.com/login")
    def open(self):
        browser.open('https://the-internet.herokuapp.com/login')
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")

    @allure.step("Fill username")
    def fill_username(self, text):
        browser.element('#username').type(text)

    @allure.step("Fill password")
    def fill_password(self, value):
        browser.element('#password').type(value)

    @allure.step("Click submit button")
    def submit(self):
        submit_button = browser.element('button[type="submit"]')  # выбираем по значению атрибута value
        web_submit_button = submit_button.locate()
        browser.driver.execute_script('arguments[0].click();', web_submit_button)

    def should_have_submission_confirmation(self):
        browser.element('#flash-messages .flash.error').should(be.visible).should(
            have.text('Your username is invalid!'))

