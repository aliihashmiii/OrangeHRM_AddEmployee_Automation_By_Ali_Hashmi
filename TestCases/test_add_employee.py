import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.LoginPage import LoginPage

@pytest.mark.smoke
def test_add_employee(setup):
    driver = setup
    driver.get("https://opensource-demo.orangehrmlive.com/")

    # --- Login to OrangeHRM ---
    login = LoginPage(driver)
    login.enter_username("Admin")
    login.enter_password("admin123")
    login.click_login()

    # --- Wait for dashboard to load ---
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[text()='Dashboard']"))
    )

    # --- Click on PIM Menu ---
    pim_menu = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='PIM']"))
    )
    pim_menu.click()

    # --- Click on "Add Employee" ---
    add_employee_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Add Employee"))
    )
    add_employee_btn.click()

    # --- Fill Employee Form ---
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "firstName"))
    ).send_keys("Ali")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "middleName"))
    ).send_keys("I.")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "lastName"))
    ).send_keys("Hashmi")

    # --- Click Save ---
    save_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )
    save_button.click()

    # --- Confirm employee added (check profile header loaded) ---
    WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Personal Details')]"))
)
print("✅ Employee added successfully: Personal Details tab is visible.")
