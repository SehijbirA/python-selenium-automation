amazon_logo = driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo' ]")
email_field = driver.find_element(By.XPATH, "//input[@id= 'ap_email' ]")
continue_button = driver.find_element(By.XPATH, "//input[@id='continue' ]")
conditions_button = driver.find_element(By.XPATH, "//a[text()='Conditions of Use' ]")
privacy_button = driver.find_element(By.XPATH, "//a[text()='Privacy Notice' ]")
need_help = driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")
forgot_password = driver.find_element(By.XPATH, "//a[@id='auth-fpp-link-bottom']")
other_issues = driver.find_element(By.XPATH, "//a[@id='ap-other-signin-issues-link']")
create_account = driver.find_element(By.XPATH, "//a[@id='createAccountSubmit']")
