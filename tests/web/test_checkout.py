from playwright.sync_api import Page, expect
from decimal import Decimal

def test_checkout_success(page: Page):
    # 1. 開啟網站並登入
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

    # 2. 加入 Sauce Labs Backpack
    backpack = page.locator(".inventory_item").filter(
        has_text="Sauce Labs Backpack"
    )
    backpack.get_by_role("button", name="Add to cart").click()

    expect(
        page.locator("[data-test='shopping-cart-badge']")
    ).to_have_text("1")

    # 3. 進入購物車並驗證商品
    page.locator("[data-test='shopping-cart-link']").click()
    expect(page).to_have_url(
        "https://www.saucedemo.com/cart.html"
    )
    cart_item = page.locator(".cart_item")
    expect(
        cart_item.get_by_text("Sauce Labs Backpack", exact=True)
    ).to_be_visible()

    # 4. 點擊 Checkout
    page.locator("[data-test='checkout']").click()

    # 5. 驗證進入結帳資訊頁
    expect(page).to_have_url(
        "https://www.saucedemo.com/checkout-step-one.html"
    )

    # 6. 填寫 First Name、Last Name、Postal Code
    page.get_by_placeholder("First Name").fill("QA")
    page.get_by_placeholder("Last Name").fill("Tester")
    page.get_by_placeholder("Zip/Postal Code").fill("10001")

    # 7. 點擊 Continue
    page.locator("[data-test='continue']").click()

    # 確認進入訂單確認頁
    expect(page).to_have_url(
        "https://www.saucedemo.com/checkout-step-two.html"
    )

    # 8. 驗證商品與金額

    # A. 確認商品存在
    expect(
        page.get_by_text("Sauce Labs Backpack", exact=True)
    ).to_be_visible()

    # B. 從網頁取得金額文字
    subtotal_text = page.locator(
        "[data-test='subtotal-label']"
    ).inner_text()

    tax_text = page.locator(
        "[data-test='tax-label']"
    ).inner_text()

    total_text = page.locator(
        "[data-test='total-label']"
    ).inner_text()

    # C. 把文字轉成可以計算的數字
    subtotal = Decimal(subtotal_text.split("$")[1])
    tax = Decimal(tax_text.split("$")[1])
    total = Decimal(total_text.split("$")[1])

    # D. 印出金額，方便觀察
    print("Subtotal:", subtotal)
    print("Tax:", tax)
    print("Total:", total)

    # E. 驗證金額是否正確相加
    assert subtotal + tax == total