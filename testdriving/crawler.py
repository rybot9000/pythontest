import requests
from bs4 import BeautifulSoup
import csv

# Initialize the data structure where to store the scraped data
products = []

# Initialize the list of discovered URLs with the first page to visit
urls = {"https://www.scrapingcourse.com/ecommerce/"}  # Use a set for uniqueness
visited_urls = set()  # Track visited URLs

# Until all pages have been visited
while urls:
    # Get the page to visit from the set
    current_url = urls.pop()
    visited_urls.add(current_url)

    try:
        # Crawling logic
        response = requests.get(current_url, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        soup = BeautifulSoup(response.content, "html.parser")

        # Discover new links
        link_elements = soup.select("a[href]")
        for link_element in link_elements:
            url = link_element["href"]
            if url.startswith("https://www.scrapingcourse.com/ecommerce/") and url not in visited_urls:
                urls.add(url)

        # If current_url is a product page
        product = {}
        product["url"] = current_url

        image_element = soup.select_one(".wp-post-image")
        name_element = soup.select_one(".product_title")
        price_element = soup.select_one(".price")

        if image_element and name_element and price_element:
            product["image"] = image_element["src"]
            product["name"] = name_element.text.strip()
            product["price"] = price_element.text.strip()

            products.append(product)

    except requests.RequestException as e:
        print(f"Error fetching {current_url}: {e}")
    except Exception as e:
        print(f"Error processing {current_url}: {e}")

# Write data to a CSV file
with open('products.csv', 'w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ["url", "image", "name", "price"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(products)
