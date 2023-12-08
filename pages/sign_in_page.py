from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class SignInPage(Page):

    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login")

    def verify_sign_in_form_is_open(self):
        assert self.find_element(*self.LOGIN_BUTTON), "Sign in form is not open"
