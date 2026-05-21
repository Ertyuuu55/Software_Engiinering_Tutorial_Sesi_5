const { test, expect } = require('@playwright/test');

test.describe('Login Functionality Tests', () => {

  test.beforeEach(async ({ page }) => {
    // Given I am on the login page
    await page.goto('https://the-internet.herokuapp.com/login');
  });

  // TEST CASE 1: Username Benar dan Password Benar (Positive Test)
  test('TC01 - Login dengan Username dan Password yang Benar', async ({ page }) => {
    /* Gherkin Syntax:
      Scenario: Successful login with valid credentials
        Given I am on the login page
        When I enter valid username "tomsmith"
        And I enter valid password "SuperSecretPassword!"
        And I click on the login button
        Then I should be redirected to the secure area page
        And I should see a success flash message "You logged into a secure area!"
    */

    // When I enter valid username "tomsmith"
    await page.locator('#username').fill('tomsmith');

    // And I enter valid password "SuperSecretPassword!"
    await page.locator('#password').fill('SuperSecretPassword!');

    // And I click on the login button
    await page.locator('button[type="submit"]').click();

    // Then I should be redirected to the secure area page
    await expect(page).toHaveURL('https://the-internet.herokuapp.com/secure');

    // And I should see a success flash message "You logged into a secure area!"
    const flashMessage = page.locator('#flash');
    await expect(flashMessage).toBeVisible();
    await expect(flashMessage).toContainText('You logged into a secure area!');
  });

  # 2. Negative Test (Username Benar, Password Salah)
  test('TC02 - Login dengan Username Benar dan Password Salah', async ({ page }) => {
    /* Gherkin Syntax:
      Scenario: Failed login with invalid password
        Given I am on the login page
        When I enter valid username "tomsmith"
        And I enter invalid password "PasswordSalah123"
        And I click on the login button
        Then I should stay on the login page
        And I should see an error flash message "Your password is invalid!"
    */

    // When I enter valid username "tomsmith"
    await page.locator('#username').fill('tomsmith');

    // And I enter invalid password "PasswordSalah123"
    await page.locator('#password').fill('PasswordSalah123');

    // And I click on the login button
    await page.locator('button[type="submit"]').click();

    // Then I should stay on the login page
    await expect(page).toHaveURL('https://the-internet.herokuapp.com/login');

    // And I should see an error flash message "Your password is invalid!"
    const flashMessage = page.locator('#flash');
    await expect(flashMessage).toBeVisible();
    await expect(flashMessage).toContainText('Your password is invalid!');
  });

});