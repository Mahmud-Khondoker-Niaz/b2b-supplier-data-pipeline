# This file defines the unified product schema
# Every product from every supplier will follow this structure

import uuid


def create_product(raw_product, variants):

    # Get basic product info
    supplier = raw_product.get("supplier", {}).get("name", "unknown")
    brand = raw_product.get("brand", {}).get("name", "unknown")

    # Get category
    category_raw = raw_product.get("categories", [{}])[0].get("name", "unknown")

    # Get product name and description from first variant
    first_variant = raw_product.get("variants", [{}])[0]
    name = first_variant.get("name", "unknown")
    description = first_variant.get("description", "unknown")

    # Build final unified product
    product = {
        "product_id":       str(uuid.uuid4()),  # unique id for each product
        "name":             name,
        "description":      description,
        "category":         category_raw,
        "brand":            brand,
        "supplier":         supplier,
        "country_of_origin": raw_product.get("country_of_origin", "unknown"),
        "variants":         variants            # list of variants from transformer
    }

    return product