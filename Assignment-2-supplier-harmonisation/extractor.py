# Fetches products from the European Sourcing API
# Uses pagination to collect 200+ products

import requests
from config import API_BASE_URL, API_TOKEN

# Every API request needs this header for authentication
HEADERS = {
    "x-auth-token": API_TOKEN,
    "Content-Type": "application/json"
}


def fetch_products(total=200):
    #Fetch products from API using pagination

    all_products = []
    page = 0

    print(f"Fetching {total} products...")

    while len(all_products) < total:

        # Request 50 products at a time
        body = {
            "lang": "en",
            "size": 50,
            "from": page * 50
        }

        response = requests.post(
            f"{API_BASE_URL}/search",
            headers=HEADERS,
            json=body
        )

        if response.status_code == 200:
            products = response.json().get("products", [])

            # Stop if no more products
            if not products:
                break

            all_products.extend(products)
            page += 1
            print(f"Page {page} done — {len(all_products)} products collected")

        else:
            print(f"Error: {response.status_code}")
            break

    print(f"Done! Total: {len(all_products)} products")
    return all_products