from selenium.webdriver.common.by import By

class InventoryPage:

    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def add_product(self):
        self.driver.find_element(*self.ADD_BACKPACK).click()

    def go_to_cart(self):
        self.driver.find_element(*self.CART).click()