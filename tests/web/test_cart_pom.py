from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_add_product_to_cart_with_pom(page: Page):
    # Step 1：使用 LoginPage 登入
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

    # Step 2：建立 InventoryPage
    inventory_page = InventoryPage(page)

    # Step 3：加入指定商品
    inventory_page.add_product_to_cart("Sauce Labs Backpack")

    # Step 4：驗證購物車數量
    expect(inventory_page.cart_badge).to_have_text("1")

    # Step 5：進入購物車
    inventory_page.open_cart()

    # Step 6：驗證購物車頁面
    expect(page).to_have_url(
        "https://www.saucedemo.com/cart.html"
    )

    # Step 7：確認商品存在
    cart_page = CartPage(page)

    backpack = cart_page.get_product("Sauce Labs Backpack")

    expect(
        backpack.get_by_text(
            "Sauce Labs Backpack",
            exact=True
        )
    ).to_be_visible()

