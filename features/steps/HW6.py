from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Click on the Cart icon')
def click_on_the_cart_icon(context):
    context.app.main_page.open_cart()


@then('Verify “Your cart is empty” message is shown')
def verify_cart_is_empty(context):
    context.app.cart_page.verify_cart_is_empty()




