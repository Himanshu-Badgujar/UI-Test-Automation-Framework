# 🖥️ UI Test Automation Framework

This project is a web-based UI test automation framework developed using **Selenium** and **Pytest**, designed to automate critical user journeys for a sample e-commerce application. The framework supports modular test architecture, data-driven execution, and dynamic test sequencing.

---

## 🚀 Features

-  **End-to-End Test Coverage**  
  Covers essential UI flows like login, product selection, cart management, and checkout.

-  **Page Object Model (POM)**  
  Structured test design with separate page classes for reusability and maintainability.

-  **Test Sequencing**  
  Uses `pytest-dependency` to manage logical test order and scenario dependencies.

-  **Data-Driven Testing**  
  Leverages JSON-based configuration for flexible input management across environments.

-  **HTML Reporting**  
  Generates detailed test execution reports using `pytest-html`, with optional screenshots on failure.

---

## 🔧 Technologies Used

- **Language:** Python 3.x  
- **Automation Tool:** Selenium  
- **Test Framework:** Pytest  
- **Report Tool:** pytest-html  
- **Design Pattern:** Page Object Model (POM)

---

## ⚙️ How to Run

1. Clone the repository  
2. Set up a virtual environment and install dependencies  
3. Run test cases using:
```bash
pytest --html=report.html
```

---

## 📌 Notes

- Ensure browser drivers (e.g., ChromeDriver) are installed and configured in system PATH.
- Customize test data and selectors through JSON config and Page Object files.
- Framework is scalable for testing any web-based application.

---

## 🧑‍💻 Author

**Himanshu Badgujar**