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
    assert len(links) == number , f"Expected {number} Links got {len(links)} Links"


@when('Click on the Search button')
def click_the_search_button(context):
    context.app.main_page.search("toothpaste")


@when('Search for toothpaste')
def search_for_product(context):
    context.driver.find_element(By.ID, "search").click()
    context.driver.find_element( By.ID,"search").send_keys("toothpaste")
    context.driver.find_element(By.CSS_SELECTOR, "button[data-test='@web/Search/SearchButton']").click()
    sleep(5)


@when('Click on the toothpaste')
def click_on_the_product(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[aria-label='Crest Pro-Health Advanced Gum Protection Toothpaste']").click()


@when('Click add to cart button')
def click_on_add_to_cart_button (context):
    sleep(10)
    context.driver.find_element(By.CSS_SELECTOR, "button[aria-label='Add to cart for Crest Pro-Health Advanced Gum Protection Toothpaste 2pk/5.1oz'").click()


@then('Verify the item is in the cart')
def verify_item_in_cart (context):
    #context.driver.find_element(By.CSS_SELECTOR, "a[href='/cart']").click()
    assert context.driver.find_element(By.CSS_SELECTOR, "div[data-test='cartItem-title']")