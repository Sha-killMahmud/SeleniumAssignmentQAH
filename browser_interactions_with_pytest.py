import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture(scope="session")
def setup_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_input_fill(setup_driver):
    driver = setup_driver
    driver.get("https://demoqa.com/text-box")
    driver.find_element(By.ID, "userName").send_keys("Shakil")
    driver.find_element(By.ID, "userEmail").send_keys("shakil@facebook.com")
    driver.find_element(By.ID, "currentAddress").send_keys("New Market, Dhaka")
    driver.find_element(By.ID, "permanentAddress").send_keys("Nawabganj, Dhaka")
    driver.find_element(By.ID, "submit").click()
    time.sleep(1)

def test_radio_button(setup_driver):
    driver = setup_driver
    driver.get("https://demoqa.com/radio-button")
    driver.find_element(By.XPATH, "//label[@for='yesRadio']").click()
    time.sleep(1)

def test_checkbox(setup_driver):
    driver = setup_driver
    driver.get("https://demoqa.com/checkbox")
    driver.find_element(By.XPATH, "//span[@class='rct-checkbox']").click()
    time.sleep(1)

def test_buttons(setup_driver):
    driver = setup_driver
    driver.get("https://demoqa.com/buttons")
    action = ActionChains(driver)
    action.double_click(driver.find_element(By.ID, "doubleClickBtn")).perform()
    action.context_click(driver.find_element(By.ID, "rightClickBtn")).perform()
    driver.find_element(By.XPATH, "//button[text()='Click Me']").click()
    time.sleep(1)

def test_hovers(setup_driver):
    driver = setup_driver
    driver.get("https://demoqa.com/tool-tips")
    action = ActionChains(driver)
    action.move_to_element(driver.find_element(By.ID, "toolTipButton")).perform()
    time.sleep(1)

def test_file_upload(setup_driver):
    driver = setup_driver
    driver.get("https://demoqa.com/upload-download")
    driver.find_element(By.ID, "uploadFile").send_keys("C:\\Users\\pc\\Downloads\\A.pdf")
    time.sleep(1)

def test_alerts(setup_driver):
    driver = setup_driver
    driver.get("https://demoqa.com/alerts")
    driver.find_element(By.ID, "alertButton").click()
    driver.switch_to.alert.accept()

    driver.find_element(By.ID, "confirmButton").click()
    driver.switch_to.alert.dismiss()

    driver.find_element(By.ID, "promtButton").click()
    alert = driver.switch_to.alert
    alert.send_keys("Shakil")
    alert.accept()
    time.sleep(1)

def test_time_alerts(setup_driver):
    driver = setup_driver
    driver.get("https://demoqa.com/alerts")
    driver.find_element(By.ID, "timerAlertButton").click()
    WebDriverWait(driver,10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()
    time.sleep(1)

def test_enable_after(setup_driver):
    driver = setup_driver
    driver.get("https://demoqa.com/dynamic-properties")
    element = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, "enableAfter")))
    element.click()
    time.sleep(1)

def test_visible_after(setup_driver):
    driver = setup_driver
    driver.get("https://demoqa.com/dynamic-properties")
    element = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, "visibleAfter")))
    element.click()
    time.sleep(1)

def test_navigation(setup_driver):
    driver = setup_driver
    driver.get("https://demoqa.com/text-box")
    driver.get("https://demoqa.com/checkbox")
    driver.back()
    driver.forward()
    driver.refresh()
    time.sleep(1)

def test_screenshot(setup_driver):
    driver = setup_driver
    driver.get("https://demoqa.com/links")
    driver.save_screenshot("ss.png")
    time.sleep(1)

def test_modals(setup_driver):
    driver = setup_driver
    driver.get("https://demoqa.com/modal-dialogs")
    driver.find_element(By.ID, "showSmallModal").click()
    driver.find_element(By.ID, "closeSmallModal").click()
    driver.find_element(By.ID, "showLargeModal").click()
    driver.find_element(By.ID, "closeLargeModal").click()
    time.sleep(1)


def test_dropdowns(setup_driver):
    driver = setup_driver
    driver.get("https://demoqa.com/select-menu")
    driver.find_element(By.XPATH, "//div[text()='Select Option']").click()
    driver.find_element(By.XPATH, "//div[text()='Group 1, option 1']").click()

    oldStyle = Select(driver.find_element(By.ID, "oldSelectMenu"))
    oldStyle.select_by_visible_text("Green")
    time.sleep(1)


def test_new_tab(setup_driver):
    driver = setup_driver
    driver.get("https://demoqa.com/browser-windows")
    driver.find_element(By.ID, "tabButton").click()
    parent = driver.current_window_handle
    all_tabs = driver.window_handles

    for tab in all_tabs:
        if tab != parent:
            driver.switch_to.window(tab)
            driver.close()
        time.sleep(1)

    driver.switch_to.window(parent)

def test_new_window(setup_driver):
    driver = setup_driver
    driver.get("https://demoqa.com/browser-windows")
    driver.find_element(By.ID, "windowButton").click()
    parent = driver.current_window_handle
    all_windows = driver.window_handles

    for win in all_windows:
        if win != parent:
            driver.switch_to.window(win)
            driver.close()
        time.sleep(1)

    driver.switch_to.window(parent)


def test_date_selector(setup_driver):
    driver = setup_driver
    driver.get("https://demoqa.com/date-picker")
    driver.find_element(By.ID, "datePickerMonthYearInput").click()
    driver.find_element(By.XPATH, "//div[text()='30']").click()
    time.sleep(1)

