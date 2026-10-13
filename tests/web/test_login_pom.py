import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


def test_login_with_pom(page: Page):
    login_page = LoginPage(page)

    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )


@pytest.mark.parametrize(
    "username,password,expected_error",
    [
        (
            "standard_user",
            "wrong_password",
            "Epic sadface: Username and password do not match any user in this service"
        ),
        (
            "",
            "secret_sauce",
            "Epic sadface: Username is required"
        ),
        (
            "standard_user",
            "",
            "Epic sadface: Password is required"
        ),
    ],
    ids=[
        "invalid_password",
        "empty_username",
        "empty_password"
    ]
)
def test_login_invalid_with_pom(
    page: Page,
    username,
    password,
    expected_error
):
    # Step 1: 建立 LoginPage 物件
    login_page = LoginPage(page)

    # Step 2: 執行登入
    login_page.login(username, password)

    # Step 3: 驗證仍停留在登入頁
    expect(page).to_have_url(
        "https://www.saucedemo.com/"
    )

    # Step 4: 驗證錯誤訊息
    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_have_text(expected_error)