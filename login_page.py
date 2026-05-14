from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
        # Selectores
        self.user_input = (By.ID, "user-name")
        self.pass_input = (By.ID, "password")
        self.login_btn = (By.ID, "login-button")
        self.error_msg = (By.CSS_SELECTOR, "[data-test='error']")
        
    def open(self):
        self.driver.get("https://saucedemo.com")
        
    def login(self, username, password):
        self.wait.until(EC.visibility_of_element_located(self.user_input)).send_keys(username)
        self.driver.find_element(*self.pass_input).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.login_btn)).click()
        
    def get_error_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.error_msg)).text
