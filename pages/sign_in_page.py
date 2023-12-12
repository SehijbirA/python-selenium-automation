from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class SignInPage(Page):

    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login")
    TERMS_AND_CONDITIONS = (By.CSS_SELECTOR, "[aria-label='terms & conditions - opens in a new window']")

    def verify_sign_in_form_is_open(self):
        assert self.find_element(*self.LOGIN_BUTTON), "Sign in form is not open"

    def open_sign_in_page(self):
        (self.open_url("https://www.target.com/account"))

    def open_terms_and_conditions(self):
        self.click(*self.TERMS_AND_CONDITIONS)

