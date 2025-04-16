import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected



class TestBase:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click(self, locator):
        self.wait.until(expected.element_to_be_clickable(locator)).click()
        time.sleep(2)

    def type(self, locator, value):
        self.wait.until(expected.visibility_of_element_located(locator)).send_keys(value)

    def get_text(self, locator):
        return self.driver.find_element(*locator).text
