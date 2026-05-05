
from selenium.webdriver.common.by import By

class CheckoutPage:

    FIRST = (By.ID, "first-name")
    LAST = (By.ID, "last-name")
    ZIP = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")
    FINISH = (By.ID, "finish")

    def __init__(self, driver):
        self.driver = driver

    def fill(self):
        self.driver.find_element(*self.FIRST).send_keys("João")
        self.driver.find_element(*self.LAST).send_keys("Silva")
        self.driver.find_element(*self.ZIP).send_keys("64000-000")
        self.driver.find_element(*self.CONTINUE).click()

    def finish(self):
        self.driver.find_element(*self.FINISH).click()