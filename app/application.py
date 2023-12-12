from pages.base_page import Page
from pages.main_page import MainPage
from pages.search_results import SearchResults
from pages.cart_page import CartPage
from pages.sign_in_page import SignInPage


class Application:
    def __init__(self, driver):
        self.search_results = SearchResults(driver)
        self.base_page = Page(driver)
        self.main_page = MainPage(driver)
        self.cart_page = CartPage(driver)
        self.sign_in_page = SignInPage(driver)
