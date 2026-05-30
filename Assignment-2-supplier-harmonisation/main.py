# main.py
# Runs the full pipeline step by step
# Fetch → Transform → Save

import pandas as pd
import json
from extractor import fetch_products
from transformer import transform_all
from models import create_product


def main():

    print("Pipeline Starting...")

    #Fetch products from API
    print("\nFetching products...")
    raw_products = fetch_products(total=200)

    # Save raw data to cache for explorer.py
    with open('output/raw_products.json', 'w') as f:
        json.dump(raw_products, f, indent=2)
    print("Raw data saved to output/raw_products.json")

    #Transform into unified schema
    print("\nTransforming products...")
    unified_products = []

    for raw_product in raw_products:
        # transform_all returns list of lists 
        variants = transform_all([raw_product])
        flat_variants = [v for sublist in variants for v in sublist]

        product = create_product(raw_product, flat_variants)
        unified_products.append(product)

    print(f"{len(unified_products)} products transformed")

    #Save as JSON
    print("\nSaving output...")
    with open('output/unified_catalogue.json', 'w') as f:
        json.dump(unified_products, f, indent=2)
    print("Saved to output/unified_catalogue.json")

    # Save as CSV
    df = pd.json_normalize(unified_products, record_path=['variants'],
                       meta=['product_id', 'name', 'category'])
    df.to_csv('output/unified_catalogue.csv', index=False)

    print("\nPipeline Complete!")


if __name__ == "__main__":
    main()