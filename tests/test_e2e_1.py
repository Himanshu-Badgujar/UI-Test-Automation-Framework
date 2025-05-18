import pytest
from pages.cart_page import CartTest
from pages.login_page import LoginTest
from pages.checkout_page import CheckoutTest
from utils.data_reader import read_json
from pages.inventory_page import InventoryTest

test_data = read_json("utils/configs/test_e2e_1_config.json")


@pytest.mark.usefixtures("driver")
class TestUI:

    def setup_method(self):
        self.login_page = LoginTest(self.driver)
        self.inventory_page = InventoryTest(self.driver)
        self.cart_page = CartTest(self.driver)
        self.checkout_page = CheckoutTest(self.driver)

    @pytest.mark.dependency(name="open_login_page")
    @pytest.mark.parametrize("user", test_data)
    def test_login_screen(self, user):
        self.driver.get(user["link"])
        assert user["link"] in self.driver.current_url

    @pytest.mark.dependency(name="login", depends=["open_login_page"])
    @pytest.mark.parametrize("user", test_data)
    def test_validate_login(self, user):
        self.login_page.login(user["username"], user["password"])
        assert "inventory.html" in self.driver.current_url

    @pytest.mark.dependency(name="add_to_cart", depends=["login"])
    def test_add_to_cart(self):
        assert self.inventory_page.add_to_cart() == "Remove"

    @pytest.mark.dependency(name="cart", depends=["add_to_cart"])
    def test_click_cart(self):
        self.inventory_page.click_cart()
        assert "cart.html" in self.driver.current_url

    @pytest.mark.dependency(name="click_checkout", depends=["cart"])
    def test_click_checkout(self):
        self.cart_page.click_checkout()
        assert "checkout-step-one.html" in self.driver.current_url

    @pytest.mark.dependency(name="checkout_step_1", depends=["click_checkout"])
    @pytest.mark.parametrize("user", test_data)
    def test_checkout_step_one(self, user):
        self.checkout_page.fill_customer_details(user["first_name"], user["last_name"], user["postal_code"])
        self.checkout_page.click_continue()
        assert "checkout-step-two.html" in self.driver.current_url

    @pytest.mark.dependency(name="checkout_step_2", depends=["checkout_step_1"])
    def test_checkout_step_two(self):
        self.checkout_page.click_finish()
        assert "checkout-complete.html" in self.driver.current_url
