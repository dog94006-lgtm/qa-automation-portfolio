from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page

        # 商品列表的共用元素
        self.products = page.locator(".inventory_item")

        # 購物車數量
        self.cart_badge = page.locator(
            "[data-test='shopping-cart-badge']"
        )

        # 購物車連結
        self.cart_link = page.locator(
            "[data-test='shopping-cart-link']"
        )

    def add_product_to_cart(self, product_name):
        product = self.products.filter(
            has_text=product_name
        )

        product.get_by_role(
            "button",
            name="Add to cart"
        ).click()

    def open_cart(self):
        self.cart_link.click()