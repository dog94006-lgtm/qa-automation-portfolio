from playwright.sync_api import Page, expect


def test_add_product_to_cart(page: Page):
    # Step 1: 開啟 SauceDemo
    page.goto("https://www.saucedemo.com/")

    # Step 2: 登入
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    # Step 3: 驗證進入商品列表
    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

    # Step 4: 找到 Backpack 商品區塊
    backpack = page.locator(".inventory_item").filter(
        has_text="Sauce Labs Backpack"
    )

    # Step 5: 點擊該商品的 Add to cart
    backpack.get_by_role("button", name="Add to cart").click()

    expect(
        page.locator("[data-test='shopping-cart-badge']")
    ).to_have_text("1")

    # Step 6: 進入購物車
    page.locator("[data-test='shopping-cart-link']").click()

    # Step 7: 確認已經進入購物車頁面
    expect(page).to_have_url(
        "https://www.saucedemo.com/cart.html"
    )

    # Step 8: 確認購物車裡有指定商品
    cart_item = page.locator(".cart_item")

    expect(
        cart_item.get_by_text("Sauce Labs Backpack", exact=True)
    ).to_be_visible()