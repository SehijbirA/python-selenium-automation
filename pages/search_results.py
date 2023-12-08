from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class SearchResults(Page):

    SEARCH_RESULT_TXT = (By.CSS_SELECTOR, "[data-test='resultsHeading']")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='chooseOptionsButton']")
    ADD_TO_CART_BTN_SIDEBAR = (By.CSS_SELECTOR,
                               "[id*='addToCartButtonOrTextIdFor'][aria-label*='Add to cart for']")
    VIEW_CART_BUTTON = (By.CSS_SELECTOR, "[href='/cart']")

    def verify_search_result(self, product):
        search_result_header = self.find_element(*self.SEARCH_RESULT_TXT).text
        assert product in search_result_header , f"Expected text {product} not found in {search_result_header}"

    def verify_search_url(self, expected_keyword):
        assert expected_keyword in self.driver.current_url, \
            f"Expected {expected_keyword} not in {self.driver.current_url}"

    def add_to_cart(self):
        self.click(*self.ADD_TO_CART_BTN)

    def add_to_cart_from_sidebar(self):
        self.click(*self.ADD_TO_CART_BTN_SIDEBAR)

    def view_cart_from_sidebar(self):
        self.click(*self.VIEW_CART_BUTTON)

        