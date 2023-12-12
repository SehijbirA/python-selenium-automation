from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open sign in page')
def open_sign_in_page(context):
    context.app.sign_in_page.open_sign_in_page()


@when('Store original windows')
def store_original_windows(context):
    context.original_window = context.app.base_page.save_current_window()


@when('Click on Target terms and conditions link')
def click_on_terms_and_conditions(context):
    context.app.sign_in_page.open_terms_and_conditions()


@when('Switch to the newly opened window')
def switch_to_newly_opened_window(context):
    context.app.base_page.switch_to_new_window()


@then('Verify Terms and Conditions page is opened')
def verify_terms_and_conditions_page_is_open(context):
    context.app.base_page.verify_partial_url("/www.target.com/c/terms-conditions/")


@then('User can close new window and switch back to original')
def close_terms_and_conditions_and_switch_to_original_page(context):
    context.app.base_page.close_page()
    context.app.base_page.switch_to_window(context.original_window)