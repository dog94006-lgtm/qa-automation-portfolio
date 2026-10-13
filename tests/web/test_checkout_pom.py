from decimal import Decimal

from playwright.sync_api import Page, expect

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_complete_checkout_with_pom(page: Page):
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

    inventory_page = InventoryPage(page)
    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    expect(inventory_page.cart_badge).to_have_text("1")
    inventory_page.open_cart()

    expect(page).to_have_url(
        "https://www.saucedemo.com/cart.html"
    )

    cart_page = CartPage(page)
    backpack = cart_page.get_product("Sauce Labs Backpack")
    expect(
        backpack.get_by_text("Sauce Labs Backpack", exact=True)
    ).to_be_visible()

    cart_page.checkout()
    expect(page).to_have_url(
        "https://www.saucedemo.com/checkout-step-one.html"
    )

    checkout_page = CheckoutPage(page)
    checkout_page.fill_customer_info("QA", "Tester", "10001")
    checkout_page.continue_checkout()

    expect(page).to_have_url(
        "https://www.saucedemo.com/checkout-step-two.html"
    )
    expect(
        page.get_by_text("Sauce Labs Backpack", exact=True)
    ).to_be_visible()

    subtotal = Decimal(
        checkout_page.subtotal_label.inner_text().split("$")[1]
    )
    tax = Decimal(
        checkout_page.tax_label.inner_text().split("$")[1]
    )
    total = Decimal(
        checkout_page.total_label.inner_text().split("$")[1]
    )

    assert subtotal + tax == total

    checkout_page.finish_checkout()
    expect(page).to_have_url(
        "https://www.saucedemo.com/checkout-complete.html"
    )
    expect(checkout_page.complete_message).to_be_visible()
