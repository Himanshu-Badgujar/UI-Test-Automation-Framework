from test_base.test_base import TestBase
from selenium.webdriver.common.by import By


class InventoryTest(TestBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.add_to_cart_button = (By.ID, "add-to-cart-sauce-labs-bike-light")
        self.remove_button = (By.ID, "remove-sauce-labs-bike-light")
        self.cart_button = (By.CLASS_NAME, "shopping_cart_link")

    def add_to_cart(self):
        self.click(self.add_to_cart_button)
        return self.get_text(self.remove_button)

    def click_cart(self):
        self.click(self.cart_button)
