from selenium.webdriver.support import expected_conditions
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait

class BasePage():
    def __init__(self, driver:WebDriver, wait:WebDriverWait):
        self.driver = driver
        self.wait = wait

    def click(self, locator):
        self.wait.until(expected_conditions.element_to_be_clickable(locator)).click()
    
    def type(self, locator, text):
        self.wait.until(expected_conditions.visibility_of_element_located(locator)).send_keys(text) 
    
    def get_text(self,locator):
        return self.wait.until(expected_conditions.visibility_of_element_located(locator)).text