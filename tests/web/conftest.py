import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


@pytest.fixture
def logged_in_page(page: Page):
    login_page = LoginPage(page)

    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

    return page