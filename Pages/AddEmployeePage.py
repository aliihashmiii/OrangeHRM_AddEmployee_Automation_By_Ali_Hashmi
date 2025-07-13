from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddEmployeePage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = (By.NAME, "firstName")
        self.middle_name_input = (By.NAME, "middleName")
        self.last_name_input = (By.NAME, "lastName")
        self.save_button = (By.XPATH, "//button[@type='submit']")

    def enter_first_name(self, first_name):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.first_name_input)
        ).send_keys(first_name)

    def enter_middle_name(self, middle_name):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.middle_name_input)
        ).send_keys(middle_name)

    def enter_last_name(self, last_name):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.last_name_input)
        ).send_keys(last_name)

    def click_save(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.save_button)
        ).click()
