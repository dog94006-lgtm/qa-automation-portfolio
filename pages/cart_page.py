from playwright.sync_api import Page


class CartPage:
    def __init__(self, page: Page):
        self.page = page

        # TODO 1：定義購物車商品區塊 Locator
        self.cart_items = page.locator(".cart_item")

        # TODO 2：定義 Checkout 按鈕 Locator
        self.checkout_button = page.locator("[data-test='checkout']")

    def get_product(self, product_name):
        # TODO 3：找到指定商品區塊
        return self.cart_items.filter(
            has_text=product_name
        )

    def checkout(self):
        # TODO 4：點擊 Checkout
        self.checkout_button.click()