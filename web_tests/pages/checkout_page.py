
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:

    FIRST = (By.ID, "first-name")
    LAST = (By.ID, "last-name")
    ZIP = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")
    FINISH = (By.ID, "finish")

    def __init__(self, driver):
        self.driver = driver

    def fill(self):
        wait = WebDriverWait(self.driver, 15)
        element = wait.until(
            EC.visibility_of_element_located(self.FIRST)
        )
        element.clear()
        element.send_keys("João")

        self.driver.find_element(*self.LAST).send_keys("Silva")
        self.driver.find_element(*self.ZIP).send_keys("64000-000")
        self.driver.find_element(*self.CONTINUE).click()

    def finish(self):
        wait = WebDriverWait(self.driver, 10)
        btn_finish = wait.until(EC.element_to_be_clickable(self.FINISH))
        btn_finish.click()