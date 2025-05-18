import os
import time
import pytest
import base64
from selenium import webdriver
from pytest_html import extras as pytest_html
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def driver(request):
    print("\n[SETUP] Launching browser...")

    options = Options()
    options.add_argument("--incognito")

    service = Service()

    driver = webdriver.Chrome(service=service, options=options)

    driver.maximize_window()
    request.cls.driver = driver

    yield driver
    time.sleep(5)

    print("\n[TEARDOWN] Closing browser...")
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    driver = getattr(item.cls, "driver", None)

    if rep.when == "call" and driver:
        screenshot_dir = "../reports/screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)

        file_name = os.path.join(screenshot_dir, f"{item.name}.png")
        driver.save_screenshot(file_name)

        with open(file_name, "rb") as f:
            encoded = base64.b64encode(f.read()).decode("utf-8")
            html = f'<div><img src="data:image/png;base64,{encoded}" alt="screenshot" style="width:300px;height:auto;" /></div>'
            extra = getattr(rep, "extra", [])
            extra.append(pytest_html.html(html))
            rep.extra = extra
