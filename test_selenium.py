from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def setup_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

def full_name(driver): # //tagname
    driver.get("https://demoqa.com/text-box")
    driver.find_element(By.XPATH, "//input").send_keys("Shakil")
    time.sleep(2)

def full_name1(driver): # //tagname[@attribute='value']
    driver.find_element(By.ID, "userName").send_keys("Mahmud")
    time.sleep(2)

def submit(driver): # //tagname[text()='text_value']
    driver.find_element(By.XPATH, "//button[text()='Submit']").click()
    time.sleep(2)

def email(driver): # //tagname[contains(@attribute,'value')]
    driver.find_element(By.XPATH, "//input[contains(@placeholder, 'name')]").send_keys("shakil@email.com")
    time.sleep(2)

def current_address(driver): # //tagname[starts-with(@attribute, 'value')]
    driver.find_element(By.XPATH, "//textarea[starts-with(@placeholder, 'Current')]").send_keys("New Market")
    time.sleep(2)

def permanent_address(driver): # //tagname[@type='text' and @name='username']
    driver.find_element(By.XPATH, "//textarea[@id='permanentAddress' and @class = 'form-control']").send_keys("Dhaka")
    time.sleep(2)

driver = setup_driver()
full_name(driver)
full_name1(driver)
email(driver)
current_address(driver)
permanent_address(driver)
submit(driver)

driver.quit()
