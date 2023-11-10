# Created by sehij at 11/9/23
Feature: Target cart and sign in tests

  Scenario: Verify “Your cart is empty” message is shown
    Given Open target.com
    When Click on the Cart icon
    Then Verify “Your cart is empty” message is shown


  Scenario: Verify that logged out user can access Sign In
    Given Open target.com
    When Click Sign In
    And Click Sign In from navigation menu
    Then Verify Sign In form opened
