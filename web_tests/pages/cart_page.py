from selenium.webdriver.common.by import By

class CartPage:

    CHECKOUT = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver

    def checkout(self):
        self.driver.find_element(*self.CHECKOUT).click()