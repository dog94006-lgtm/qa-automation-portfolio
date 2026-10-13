from playwright.sync_api import Page


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page

        # Checkout Information
        self.first_name_input = page.get_by_placeholder("First Name")
        self.last_name_input = page.get_by_placeholder("Last Name")
        self.postal_code_input = page.get_by_placeholder("Zip/Postal Code")
        self.continue_button = page.locator("[data-test='continue']")

        # Checkout Overview
        self.subtotal_label = page.locator("[data-test='subtotal-label']")
        self.tax_label = page.locator("[data-test='tax-label']")
        self.total_label = page.locator("[data-test='total-label']")
        self.finish_button = page.locator("[data-test='finish']")

        # Checkout Complete
        self.complete_message = page.get_by_text(
            "Thank you for your order!",
            exact=True
        )

    def fill_customer_info(self, first_name, last_name, postal_code):
        # TODO 1: 填入 First Name
        self.first_name_input.fill(first_name)
        # TODO 2: 填入 Last Name
        self.last_name_input.fill(last_name)
        # TODO 3: 填入 Postal Code
        self.postal_code_input.fill(postal_code)

    def continue_checkout(self):
        # TODO 4: 點擊 Continue
        self.continue_button.click()

    def finish_checkout(self):
        # TODO 5: 點擊 Finish
        self.finish_button.click()