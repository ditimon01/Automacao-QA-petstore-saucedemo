from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:

    CHECKOUT = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver

    def checkout(self):
        wait = WebDriverWait(self.driver, 10)

        btn = wait.until(EC.element_to_be_clickable(self.CHECKOUT))
        btn.click()