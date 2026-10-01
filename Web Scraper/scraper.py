import requests
from bs4 import BeautifulSoup

# URL of the product page (Practice sandbox)
URL = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

# Headers to mimic a real browser
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

def check_price():
    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")
    
    # 1. Extract Product Title
    title = soup.find("h1").get_text()
    
    # 2. Extract Product Price
    price_text = soup.find("p", class_="price_color").get_text()
    # Convert price string (e.g. £51.77) to float
    price = float(price_text.replace("£", "").replace("$", ""))
    
    print(f"Product: {title}")
    print(f"Current Price: ${price}")
    
    # 3. Target Price Condition
    target_price = 55.0
    if price < target_price:
        print("🚨 Deal Alert! The price has dropped!")
    else:
        print("No discount yet. Still waiting...")

if __name__ == "__main__":
    check_price()