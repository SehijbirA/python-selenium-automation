# Created by sehij at 12/6/23
Feature: Test cases for the cart page

  Scenario: “Your cart is empty” message is shown for empty cart
    Given Open target.com
    Then Click on the Cart icon
    Then Verify “Your cart is empty” message is shown
