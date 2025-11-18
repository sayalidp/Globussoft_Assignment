import requests
from bs4 import BeautifulSoup
import csv
import datetime

def scrape_amazon_laptops():
    url = "https://www.amazon.in/s?k=laptop"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
        "Accept-Language": "en-US, en;q=0.5"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    results = soup.find_all("div", {"data-component-type": "s-search-result"})

    data = []

    for item in results:
        # Title
        title_tag = item.h2
        title = title_tag.text.strip() if title_tag else "N/A"

        # Image
        img_tag = item.find("img", {"class": "s-image"})
        image = img_tag["src"] if img_tag else "N/A"

        # Rating
        rating_tag = item.find("span", {"class": "a-icon-alt"})
        rating = rating_tag.text.strip() if rating_tag else "N/A"

        # Price
        price_tag = item.find("span", {"class": "a-price-whole"})
        price = price_tag.text.strip() if price_tag else "N/A"

        # Ad / Organic
        ad_tag = item.find("span", {"class": "s-sponsored-label-text"})
        ad_or_organic = "Ad" if ad_tag else "Organic"

        data.append([title, image, rating, price, ad_or_organic])

    # Save CSV with timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"amazon_laptops_{timestamp}.csv"

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Image URL", "Rating", "Price", "Ad/Organic"])
        writer.writerows(data)

    print(f"Data scraped successfully! File saved as {filename}")


if __name__ == "__main__":
    scrape_amazon_laptops()
