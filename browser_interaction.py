import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


def setup_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

def input_fill(driver):
    driver.get("https://demoqa.com/text-box")
    driver.find_element(By.ID, "userName").send_keys("Shakil")
    driver.find_element(By.ID, "userEmail").send_keys("shakil@facebook.com")
    driver.find_element(By.ID, "currentAddress").send_keys("New Market, Dhaka")
    driver.find_element(By.ID, "permanentAddress").send_keys("Nawabganj, Dhaka")
    driver.find_element(By.ID, "submit").click()
    time.sleep(2)

def radio_button(driver):
    driver.get("https://demoqa.com/radio-button")
    driver.find_element(By.XPATH, "//label[@for='yesRadio']").click()
    time.sleep(2)

def checkbox(driver):
    driver.get("https://demoqa.com/checkbox")
    driver.find_element(By.XPATH, "//span[@class='rct-checkbox']").click()
    time.sleep(2)

def buttons(driver):
    driver.get("https://demoqa.com/buttons")
    action = ActionChains(driver)
    action.double_click(driver.find_element(By.ID, "doubleClickBtn")).perform()
    time.sleep(1)
    action.context_click(driver.find_element(By.ID, "rightClickBtn")).perform()
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[text()='Click Me']").click()
    time.sleep(2)

def hovers(driver):
    driver.get("https://demoqa.com/tool-tips")
    action = ActionChains(driver)
    action.move_to_element(driver.find_element(By.ID, "toolTipButton")).perform()
    time.sleep(2)

def file_upload(driver):
    driver.get("https://demoqa.com/upload-download")
    driver.find_element(By.ID, "uploadFile").send_keys("C:\\Users\\pc\\Downloads\\A.pdf")
    time.sleep(2)

def alerts(driver):
    driver.get("https://demoqa.com/alerts")
    driver.find_element(By.ID, "alertButton").click()
    time.sleep(2)
    driver.switch_to.alert.accept()

    driver.find_element(By.ID, "confirmButton").click()
    time.sleep(2)
    driver.switch_to.alert.dismiss()
    time.sleep(2)


    driver.find_element(By.ID, "promtButton").click()
    time.sleep(2)
    alert = driver.switch_to.alert
    time.sleep(1)
    alert.send_keys("Shakil")
    time.sleep(2)
    alert.accept()
    time.sleep(2)

def time_alerts(driver):
    driver.get("https://demoqa.com/alerts")
    driver.find_element(By.ID, "timerAlertButton").click()
    WebDriverWait(driver,10).until(EC.alert_is_present())
    time.sleep(1)
    driver.switch_to.alert.accept()
    time.sleep(1)

def enable_after(driver):
    driver.get("https://demoqa.com/dynamic-properties")
    element = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, "enableAfter")))
    element.click()
    time.sleep(2)

def visible_after(driver):
    driver.get("https://demoqa.com/dynamic-properties")
    element = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, "visibleAfter")))
    element.click()
    time.sleep(2)

def navigation(driver):
    driver.get("https://demoqa.com/text-box")
    time.sleep(2)
    driver.get("https://demoqa.com/checkbox")
    time.sleep(2)
    driver.back()
    time.sleep(2)
    driver.forward()
    time.sleep(2)
    driver.refresh()
    time.sleep(2)

def screenshot(driver):
    driver.get("https://demoqa.com/links")
    driver.save_screenshot("ss.png")
    time.sleep(2)

def modals(driver):
    driver.get("https://demoqa.com/modal-dialogs")
    driver.find_element(By.ID, "showSmallModal").click()
    time.sleep(2)
    driver.find_element(By.ID, "closeSmallModal").click()

    driver.find_element(By.ID, "showLargeModal").click()
    time.sleep(2)
    driver.find_element(By.ID, "closeLargeModal").click()
    time.sleep(2)


def dropdowns(driver):
    driver.get("https://demoqa.com/select-menu")
    driver.find_element(By.XPATH, "//div[text()='Select Option']").click()
    driver.find_element(By.XPATH, "//div[text()='Group 1, option 1']").click()

    time.sleep(2)

    oldStyle = Select(driver.find_element(By.ID, "oldSelectMenu"))
    oldStyle.select_by_visible_text("Green")
    time.sleep(2)


def new_tab(driver):
    driver.get("https://demoqa.com/browser-windows")
    driver.find_element(By.ID, "tabButton").click()
    time.sleep(1)
    parent = driver.current_window_handle
    all_tabs = driver.window_handles

    for tab in all_tabs:
        if tab != parent:
            driver.switch_to.window(tab)
            driver.close()
        time.sleep(1)

    driver.switch_to.window(parent)

def new_window(driver):
    driver.get("https://demoqa.com/browser-windows")
    driver.find_element(By.ID, "windowButton").click()
    time.sleep(1)
    parent = driver.current_window_handle
    all_windows = driver.window_handles

    for win in all_windows:
        if win != parent:
            driver.switch_to.window(win)
            driver.close()
        time.sleep(1)

    driver.switch_to.window(parent)


def date_selector(driver):
    driver.get("https://demoqa.com/date-picker")
    driver.find_element(By.ID, "datePickerMonthYearInput").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//div[text()='30']").click()
    time.sleep(2)


driver = setup_driver()

input_fill(driver)
radio_button(driver)
checkbox(driver)
buttons(driver)
hovers(driver)
file_upload(driver)
alerts(driver)
time_alerts(driver)
enable_after(driver)
visible_after(driver)
navigation(driver)
screenshot(driver)
modals(driver)
dropdowns(driver)
new_tab(driver)
new_window(driver)
date_selector(driver)

driver.quit()