from test_base.test_base import TestBase
from selenium.webdriver.common.by import By


class CartTest(TestBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.checkout_button = (By.ID, "checkout")

    def click_checkout(self):
        self.click(self.checkout_button)
