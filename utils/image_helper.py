from selenium.webdriver import Chrome
from datetime import datetime
import os 

def save_screenshot(driver:Chrome, name="screenshot"):
    screenshot_folder = "C:\\Tests\\Screenshots\\" + datetime.now().strftime("%d-%m-%Y")
    os.makedirs(screenshot_folder, exist_ok=True)

    file_name = f"{name}_{datetime.now().strftime("%H-%M-%S")}_{datetime.now().microsecond}.png"

    abs_path = screenshot_folder+"\\"+file_name
    driver.save_screenshot(abs_path)

    return abs_path
