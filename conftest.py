import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Chrome
from utils.image_helper import save_screenshot

@pytest.fixture
def driver():
    driver = Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture 
def wait(driver):
    wait = WebDriverWait(driver, 10)
    yield wait

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield # testi çalıştır.
    result = outcome.get_result()
    if result.when == "call":
        driver = item.funcargs.get("driver",None)
        save_screenshot(driver, item.name)