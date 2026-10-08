# QA Automation Portfolio

A personal software testing portfolio demonstrating manual test case design, API testing, and automated testing using Python and Pytest.

## Project Overview

This project documents my learning and practical experience in software quality assurance (QA).

The goal is to practice requirement analysis, test case design, API testing, defect reporting, and test automation.

## Tech Stack

- Python 3.10
- Pytest
- Requests
- Git / GitHub
- GitHub Issues

## Test Coverage

### Login Testing

- Valid and invalid credentials
- Username whitespace handling
- Password case sensitivity
- Username case insensitivity
- Parameterized testing
- Pytest fixtures

### API Testing

Using JSONPlaceholder as a public mock REST API.

- GET: Retrieve existing and nonexistent resources
- POST: Create a simulated resource
- PUT: Update a simulated resource
- DELETE: Delete a simulated resource
- Negative testing and response validation

**Note:** JSONPlaceholder simulates write operations and does not permanently save changes.

## Test Cases

[Login Requirements and Test Cases](testcases/login_requirements_and_testcases.md)

## Automated Tests

[Pytest Login Logic Tests](tests/test_login_logic.py)

[REST API Tests](tests/api/test_posts_api.py)

## Bug Investigation

[Issue #1 - PUT request to nonexistent post returns HTTP 500](https://github.com/dog94006-lgtm/qa-automation-portfolio/issues/1)

This issue documents an unexpected server response observed during negative API testing. The expected behavior requires confirmation against the API specification.

## How to Run Tests

Install the required dependencies:

```bash
python -m pip install -r requirements.txt
```

Run all tests:

```bash
python -m pytest -v
```

Run API tests only:

```bash
python -m pytest tests/api/ -v
```

## Learning Roadmap

- [x] Git and GitHub basics
- [x] Manual test case design
- [x] Pytest basics
- [x] Parameterized testing
- [x] Pytest fixtures
- [x] API CRUD testing
- [x] GitHub Issues and bug reporting
- [ ] Postman API testing
- [ ] Playwright Web UI automation
- [ ] Page Object Model (POM)
- [ ] CI/CD with GitHub Actions

## Disclaimer

This repository is a personal QA learning project using publicly available mock APIs. It is not an official test suite for JSONPlaceholder.