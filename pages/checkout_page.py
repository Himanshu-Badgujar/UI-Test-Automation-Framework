from test_base.test_base import TestBase
from selenium.webdriver.common.by import By


class CheckoutTest(TestBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.finish_button = (By.ID, "finish")

    def fill_customer_details(self, first_name, last_name, postal_code):
        self.type(self.first_name_input, first_name)
        self.type(self.last_name_input, last_name)
        self.type(self.postal_code_input, postal_code)

    def click_continue(self):
        self.click(self.continue_button)

    def click_finish(self):
        self.click(self.finish_button)
