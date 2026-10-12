# QA Automation Portfolio

A personal software testing portfolio demonstrating manual test case design, REST API testing, and Web UI automation using Python, Pytest, Postman, and Playwright.

## Project Overview

This project documents my hands-on learning and practical experience in Software Quality Assurance (QA).

The goal is to practice requirement analysis, test case design, API testing, negative testing, defect reporting, and test automation.

## Tech Stack

- **Language:** Python 3.10
- **Test Framework:** Pytest
- **API Testing:** Requests, Postman
- **Web UI Automation:** Playwright for Python
- **Version Control:** Git, GitHub
- **Defect Tracking:** GitHub Issues

## Test Coverage

### Login Logic Testing

- Valid and invalid credentials
- Username whitespace handling
- Password case sensitivity
- Username case insensitivity
- Parameterized tests
- Pytest fixtures

### REST API Testing

Using JSONPlaceholder as a public mock REST API.

- GET: Retrieve existing and nonexistent resources
- POST: Create a simulated resource
- PUT: Update a simulated resource
- DELETE: Delete a simulated resource
- Negative testing and response validation

**Note:** JSONPlaceholder simulates write operations and does not permanently save changes.

### Web UI Automation — SauceDemo

Using Playwright with Pytest to automate browser-based testing on [SauceDemo](https://www.saucedemo.com/).

**Login Testing**
- Successful login with valid credentials
- Invalid password
- Empty username
- Empty password
- Parameterized negative login tests

**Shopping Cart Testing**
- Add a selected product to the cart
- Verify shopping cart item count
- Verify the correct product exists in the cart

**Checkout E2E Testing**
- Log in and add a product to the cart
- Complete customer information form
- Verify checkout navigation
- Validate subtotal, tax, and total calculation using Python Decimal
- Complete checkout and verify the confirmation message

## Test Cases

[Login Requirements and Test Cases](testcases/login_requirements_and_testcases.md)

## Automated Test Scripts

### Python Login Logic Tests

[View Login Logic Tests](tests/test_login_logic.py)

### REST API Tests

[View API CRUD Tests](tests/api/test_posts_api.py)

### Playwright Web UI Tests

| Test File | Description |
|---|---|
| [test_browser.py](tests/web/test_browser.py) | Browser launch smoke test |
| [test_login.py](tests/web/test_login.py) | Login behavior testing |
| [test_login_parametrize.py](tests/web/test_login_parametrize.py) | Parameterized negative login tests |
| [test_cart.py](tests/web/test_cart.py) | Add-to-cart and cart validation |
| [test_checkout.py](tests/web/test_checkout.py) | Complete checkout E2E automation |

## Postman API Testing

Created a Postman collection for JSONPlaceholder API testing.

- GET existing and nonexistent resources
- POST create resource
- PUT update resource
- DELETE resource
- Environment variables
- Collection Runner: 15 assertions passed in the local test run

[View Postman Project](postman/)

## Bug Investigation

[Issue #1 — PUT Request to Nonexistent Post Returns HTTP 500](https://github.com/dog94006-lgtm/qa-automation-portfolio/issues/1)

This issue documents an unexpected server response observed during negative API testing. The expected behavior requires confirmation against the API specification.

## How to Run Tests

### 1. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 2. Run API Tests

```bash
python -m pytest tests/api/ -v
```

### 3. Run Web UI Tests

Install the Playwright-managed Chromium browser:

```bash
python -m playwright install chromium
```

Then execute:

```bash
python -m pytest tests/web/ -v
```

Alternatively, use an existing Google Chrome installation:

```bash
python -m pytest tests/web/ -v --headed --browser-channel chrome
```

### 4. Run the Complete Test Suite

When using locally installed Google Chrome:

```bash
python -m pytest -v --browser-channel chrome
```

**Note:** The Playwright browser and network access to the test websites are required when executing Web UI tests.

## Learning Roadmap

- [x] Git and GitHub basics
- [x] Manual test case design
- [x] Pytest basics
- [x] Parameterized testing
- [x] Pytest fixtures
- [x] REST API CRUD testing
- [x] GitHub Issues and bug reporting
- [x] Postman API testing
- [x] Playwright Web UI automation fundamentals
- [x] Login, cart, and checkout E2E testing
- [ ] Page Object Model (POM)
- [ ] CI/CD with GitHub Actions

## Disclaimer

This repository is a personal QA learning project using publicly available demonstration websites and mock APIs. It is not an official test suite for SauceDemo or JSONPlaceholder.