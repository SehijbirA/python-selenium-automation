from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target Circle page')
def open_target_circle(context):
    context.app.main_page.open_main()


@then('Verify there are {number} Benefits boxes')
def verify_number_of_benefits_boxes(context, number):
    number = int(number)
    links = context.driver.find_elements(By.CSS_SELECTOR, "li.styles__BenefitCard-sc-9mx6dj-2")
    assert len(links) == number, f"Expected {number} Links got {len(links)} Links"


@when('Click on the Search button')
def click_the_search_button(context):
    context.app.main_page.search("toothpaste")


@when('Search for {product}')
def search_for_product(context, product):
    context.app.main_page.search(product)


@when('Click add to cart button')
def click_on_add_to_cart_button(context):
    context.app.search_results.add_to_cart()


@when('Click on add to cart from side bar')
def click_on_add_to_cart_button_from_side_bar(context):
    context.app.search_results.add_to_cart_from_sidebar()


@then('Verify the item is in the cart')
def verify_item_in_cart(context):
    context.app.cart_page.verify_item_in_cart()


@then('Click on View Cart from the sidebar')
def click_on_view_cart_from_sidebar(context):
    context.app.search_results.view_cart_from_sidebar()