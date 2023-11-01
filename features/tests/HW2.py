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
# open sign in page

# open the Amazon URL
driver.get("https://www.amazon.com")
sleep(15)
# find and click orders
driver.find_element(By.XPATH, "//a[@id='nav-orders']").click()

# verify the sign in page is open
assert driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']")
print('Test Passed')

assert driver.find_element(By.XPATH, "//input[@id= 'ap_email' ]")
print("Test 2 Passed")

#Close the browser
driver.quit()