from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target.com')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('Click on the Cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()


@then('Verify “Your cart is empty” message is shown')
def verify_cart_is_empty(context):
    assert context.driver.find_element(By.XPATH, "//h1[contains(text(),'Your cart is empty')]"), "Cart is not empty"


@when('Click Sign In')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']").click()


@when('Click Sign In from navigation menu')
def click_sign_in_form_navigation_menu(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()


@then('Verify Sign In form opened')
def verify_sign_in_form_is_open(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "#login"), "Sign in form is not open"

