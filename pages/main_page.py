from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class MainPage(Page):

    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[data-test='@web/Search/SearchButton']")
    SEARCH_FIELD = (By.ID, "search")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "[data-test='@web/AccountLink']")
    SIGN_IN_BUTTON_SIDEBAR = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")

    def open_main(self):
        self.open_url("https://www.target.com/")

    def search(self, product):
        self.input(*self.SEARCH_FIELD, text=product)
        self.click(*self.SEARCH_BUTTON)
        sleep(6)

    def open_cart(self):
        self.click(*self.CART_ICON)

    def open_sign_in_when_signed_out(self):
        self.click(*self.SIGN_IN_BUTTON)

    def click_sign_in_form_navigation_menu(self):
        self.click(*self.SIGN_IN_BUTTON_SIDEBAR)






