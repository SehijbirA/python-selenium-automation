from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class CartPage(Page):
    EMPTY_CART_TEXT = (By.XPATH, "//h1[contains(text(),'Your cart is empty')]")
    CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")

    def verify_cart_is_empty(self):
        assert self.find_element(*self.EMPTY_CART_TEXT), f"Cart is not empty"

    def verify_item_in_cart(self):
        assert self.find_element(*self.CART_ITEM_TITLE), f"Cart is empty"
