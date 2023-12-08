from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target.com')
def open_target(context):
    context.app.main_page.open_main()


@when('Click on the Cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()


@when('Click Sign In')
def click_sign_in(context):
    context.app.main_page.open_sign_in_when_signed_out()


@when('Click Sign In from navigation menu')
def click_sign_in_form_navigation_menu(context):
    context.app.main_page.click_sign_in_form_navigation_menu()


@then('Verify Sign In form opened')
def verify_sign_in_form_is_open(context):
    context.app.sign_in_page.verify_sign_in_form_is_open()
