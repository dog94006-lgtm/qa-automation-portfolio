from playwright.sync_api import sync_playwright


def test_open_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            channel="chrome",
            headless=False
        )

        page = browser.new_page()

        page.goto("https://www.saucedemo.com/")

        print("Page title:", page.title())

        browser.close()