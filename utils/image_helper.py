from selenium.webdriver import Chrome
from datetime import datetime
import os 
from env.constants import Paths,DateFormat

def save_screenshot(driver:Chrome, name="screenshot"):
    screenshot_folder = Paths.SCREENSHOT  + datetime.now().strftime(DateFormat.DATE_FORMAT)
    os.makedirs(screenshot_folder, exist_ok=True)

    file_name = f"{name}_{datetime.now().strftime(DateFormat.TIME_FORMAT)}_{datetime.now().microsecond}.png"

    abs_path = screenshot_folder+"\\"+file_name
    driver.save_screenshot(abs_path)

    return abs_path
