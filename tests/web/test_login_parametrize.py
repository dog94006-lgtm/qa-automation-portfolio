import pytest
from playwright.sync_api import Page, expect


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
def test_login_invalid_cases(
    page: Page,
    username,
    password,
    expected_error
):
    page.goto("https://www.saucedemo.com/")

    # TODO 1: 輸入 username
    page.get_by_placeholder("Username").fill(username)
    # TODO 2: 輸入 password
    page.get_by_placeholder("Password").fill(password)
    # TODO 3: 點擊 Login
    page.get_by_role("button",name="Login").click()
    # TODO 4: 驗證仍在登入頁面
    expect(page).to_have_url("https://www.saucedemo.com/")
    # TODO 5: 驗證錯誤訊息包含 expected_error    
    error_message = page.get_by_role("alert")
    expect(error_message).to_be_visible()
    expect(error_message).to_have_text(expected_error)