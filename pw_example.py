from playwright.sync_api import sync_playwright

def run_playwright_sample():
    with sync_playwright() as p:
        # Launch browser (Chromium, Firefox, or WebKit)
        browser = p.chromium.launch(headless=True)
        # Open new browser page/tab
        page = browser.new_page()
        # Navigate to a website
        page.goto("https://example.com")
        # Wait for page to load, and extract text from the heading
        heading = page.locator("h1").inner_text()
        print(f"H1 heading text: {heading}")
        # Close browser
        browser.close()

# Run the sample
if __name__ == "__main__":
    run_playwright_sample()
