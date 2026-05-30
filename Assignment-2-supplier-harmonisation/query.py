
# This file provides simple query functions to search the unified catalogue
import json


def load_catalogue():
    #Load the unified catalogue from file
    with open('output/unified_catalogue.json', 'r') as f:
        return json.load(f)


def get_by_category(category):
    #Get all products by category
    products = load_catalogue()

    # Filter products where category matches
    results = [p for p in products if category.lower() in p.get("category", "").lower()]

    print(f"\nProducts in category: '{category}'")
    print(f"{len(results)} products")
    for p in results:
        print(f"  - {p['name']}")

    return results


def get_in_stock():

    #Get all products that have at least one variant in stock
    products = load_catalogue()

    results = []
    for product in products:
        # Check if any variant is in stock
        in_stock_variants = [v for v in product.get("variants", []) if v.get("in_stock")]
        if in_stock_variants:
            results.append(product)

    print(f"\nProducts In Stock")
    print(f" {len(results)} products")
    for p in results:
        print(f"  - {p['name']}")

    return results


def get_by_supplier(supplier):
    
    #Get all products by supplier
    products = load_catalogue()

    results = [p for p in products if supplier.lower() in p.get("supplier", "").lower()]

    print(f"\nProducts by supplier: '{supplier}'")
    print(f"Found: {len(results)} products")
    for p in results:
        print(f"  - {p['name']}")

    return results


# Test all queries
if __name__ == "__main__":
    print("Testing Query")
    get_by_category("beauty")
    get_in_stock()
    get_by_supplier("xd connects")