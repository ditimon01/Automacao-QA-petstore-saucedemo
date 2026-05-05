from selenium.webdriver.common.by import By

class LoginPage:
    URL = "https://www.saucedemo.com/"

    USER = (By.ID, "user-name")
    PASS = (By.ID, "password")
    BTN = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def login(self, user, password):
        self.driver.find_element(*self.USER).send_keys(user)
        self.driver.find_element(*self.PASS).send_keys(password)
        self.driver.find_element(*self.BTN).click()