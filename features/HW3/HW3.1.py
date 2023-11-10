from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('Https://www.Amazon.com')

# amazon logo
driver.find_element(By.CSS_SELECTOR, 'i.a-icon.a-icon-logo')

# create account
driver.find_element(By.XPATH, "//h1[contains(text(),'Create account')]")

# Your name
driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')

# email
driver.find_element(By.CSS_SELECTOR, '#ap_email')

# password
driver.find_element(By.CSS_SELECTOR, '#ap_password')

# password must be 6 characters or more
driver.find_element(By.XPATH, "//div[contains(text(),'Passwords must be at least 6 characters')]")

# re-enter password
driver.find_element(By.CSS_SELECTOR, '#ap_password_check')

# continue button
driver.find_element(By.CSS_SELECTOR, '#continue')

# conditions of use
driver.find_element(By.XPATH, "//a[contains(@href, 'condition_of_use')]")

# privacy notice
driver.find_element(By.XPATH, "//a[contains(@href, 'notification_privacy_notice')]")

# sign in
driver.find_element(By.XPATH, "//a[contains(@href, 'ap/signin')]")
