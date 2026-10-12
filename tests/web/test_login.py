from playwright.sync_api import Page, expect


def test_login_success(page: Page):
    # 1. 開啟登入頁面
    page.goto("https://www.saucedemo.com/")

    # 2. 輸入帳號
    page.locator("#user-name").fill("standard_user")

    # 3. 輸入密碼
    page.locator("#password").fill("wrong_password")

    # 4. 點擊登入按鈕
    page.locator("#login-button").click()

    error_message = page.locator("[data-test='error']")

    # 5. 驗證登入成功
    expect(page).to_have_url(
        "https://www.saucedemo.com/"
    )

    expect(error_message).to_be_visible()

    expect(error_message).to_have_text(
    "Epic sadface: Username and password do not match any user in this service"
)