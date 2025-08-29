from pages.login_page import LoginPage

class TestLogin():
    def test_successfull(self,driver,wait):
        login_page = LoginPage(driver, wait)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        assert driver.current_url == "https://www.saucedemo.com/inventory.html"
        
    def test_invalid_user(self,driver,wait):
        login_page = LoginPage(driver, wait)
        login_page.open()
        login_page.login("invalid_user", "wrong_password")