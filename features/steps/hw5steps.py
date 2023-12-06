from selenium.webdriver.common.by import By
from behave import given, when, then

COLOR_OPTIONS = (By.CSS_SELECTOR, "[class*='ButtonWrapper'] img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[class*='StyledVariationSelectorImage'] [class*='CellVariationHeaderWrapper']")

@given ('Open target product page A-88345426')
def open_product_page_88345426 (context):
    context.driver.get("https://www.target.com/p/A-88345426")


@then ('Verify each color can be selected')
def verify_each_color_can_be_selected (context):
    expected_colors = ['Brown', 'Oatmeal', 'Gray', 'Black']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)

    for color in colors:
        color.click()
        selected_color = context.driver.find_element(*SELECTED_COLOR).text.split('\n')[1]
        actual_colors.append(selected_color)

    print(expected_colors)
    print(actual_colors)
    assert expected_colors == actual_colors
