from playwright.sync_api import sync_playwright

def get_52_week_high_low_nse(symbol):
    # url = f"https://www.nseindia.com/get-quotes/equity?symbol={symbol.upper()}"
    url = f"https://www.nseindia.com/"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        # Recommended: Set a realistic user-agent to reduce chance of block
        page.set_extra_http_headers({
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        })

        page.goto(url, timeout=60000)
        page.wait_for_timeout(60000)  # wait for JavaScript to load (adjust as needed)

        # Use your browser's Inspect tool to verify the correct selector!
        # As of 2025, try for a table row containing "52 Week High/Low"
        
        try:
            # Look for the label with "52 Week High" or "52 Week Low" (Exact selectors may change)
            high_elem = page.locator('xpath=//td[contains(text(), "52 Week High")]/following-sibling::td').first
            low_elem = page.locator('xpath=//td[contains(text(), "52 Week Low")]/following-sibling::td').first

            high = high_elem.inner_text()
            low = low_elem.inner_text()

            print(f"Symbol: {symbol}")
            print(f"52 Week High: {high}")
            print(f"52 Week Low: {low}")
        except Exception as e:
            print("Error extracting 52-week high/low:", e)
        finally:
            browser.close()

# Example usage
if __name__ == "__main__":
    get_52_week_high_low_nse("RELIANCE")  # Replace with any NSE symbol
