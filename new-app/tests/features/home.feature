Feature: Sign In/Sign Up

  Scenario: Sign In
    Given Home page is open
    When I click on Sign In
    Then A pop up appears saying "You are trying to sign in!"

  Scenario: Sign Up
    Given Home page is open
    When I click on Try for Free
    Then A pop up appears saying "Try for free for 30 days!"