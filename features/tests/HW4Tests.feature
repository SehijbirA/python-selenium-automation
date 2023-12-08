# Created by sehij at 11/14/23
Feature: Target Circle, Cart, and help test cases

  Scenario: Verify there are 5 benefit boxes on the Target Circle page
    Given Open Target Circle page
    Then Verify there are 5 Benefits boxes

  Scenario: Add a product to the cart and verify it is there
    Given Open target.com
    When Search for toothpaste
    And Click add to cart button
    And Click on add to cart from side bar
    Then Click on View Cart from the sidebar
    Then Verify the item is in the cart

