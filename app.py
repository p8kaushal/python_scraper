import requests
from bs4 import BeautifulSoup

def get_52_week_high_low(stock_code):
    # Example stock_code: 'RELIANCE'
    url = f"https://www.moneycontrol.com/india/stockpricequote/refineries/{stock_code.lower()}/"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; YourBot/0.1)"
    }
    
    try:
        print("Fetching data for:", stock_code)
        print("URL:", url)
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find table or section containing 52 Week High / Low; Moneycontrol's structure may change
        high_low_section = soup.find('div', text=lambda t: t and '52 Week High' in t)
        if not high_low_section:
            print("52-week high/low section not found. The website structure may have changed.")
            return

        # Find the values (the following step is highly dependent on site’s actual HTML structure)
        parent = high_low_section.find_parent()
        values = parent.find_all('span')
        if len(values) >= 2:
            high = values[0].text.strip()
            low = values[1].text.strip()
            print(f"52 Week High for {stock_code}: {high}")
            print(f"52 Week Low for {stock_code}: {low}")
        else:
            print("Could not extract values.")
    except Exception as e:
        print("Error fetching data:", e)

# Example usage:
get_52_week_high_low('RELIANCE')  # Replace 'RELIANCE' with the stock code you want
