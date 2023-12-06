from pages.base_page import Page
from pages.main_page import MainPage
from pages.search_results import SearchResults
from pages.cart_page import CartPage

class Application:
    def __init__(self, driver):
        self.search_results_page = SearchResults(driver)
        self.page = Page(driver)
        self.main_page = MainPage(driver)
        self.cart_page = CartPage(driver)