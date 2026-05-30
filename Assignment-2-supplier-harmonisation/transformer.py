# This file standardises and harmonises raw product data from the API
# It maps supplier-specific fields into a unified schema

import uuid


# Standard color mapping
# Different suppliers use different color names , we map them to standard colors
COLOR_MAP = {
    "navy blue": "blue",
    "dark blue": "blue",
    "light blue": "blue",
    "sky blue": "blue",
    "navy": "blue",
    "scarlet": "red",
    "dark red": "red",
    "burgundy": "red",
    "olive": "green",
    "dark green": "green",
    "lime": "green",
    "charcoal": "grey",
    "dark grey": "grey",
    "light grey": "grey",
    "silver": "grey",
    "cream": "white",
    "off white": "white",
    "ivory": "white",
    "beige": "white",
    "gold": "yellow",
    "orange red": "orange",
}


# Standard category mapping
# Different suppliers use different category names , we map them to standard ones
CATEGORY_MAP = {
    "drinkware": ["mug", "mugs", "bottle", "bottles", "flask", "flasks", "cup", "cups"],
    "apparel": ["t-shirt", "jacket", "cap", "hat", "bag", "bags"],
    "technology": ["usb", "charger", "speaker", "headphone", "power bank"],
    "stationery": ["pen", "pencil", "notebook", "notepad"],
    "beauty": ["razor", "shaver", "cosmetic", "wellness"],
    "outdoor": ["umbrella", "torch", "flashlight"],
}


def normalise_color(color):
    
    if not color:
        return "unknown"

    # Convert to lowercase and remove extra spaces
    # This ensures "Navy Blue", "NAVY BLUE", "navy blue" all match
    color_lower = color.lower().strip()

    # Check if color is in our mapping
    if color_lower in COLOR_MAP:
        return COLOR_MAP[color_lower]

    return color_lower


def normalise_category(category):
    
    if not category:
        return "uncategorized"

    category_lower = category.lower().strip()

    # Check if category matches any standard category
    for standard_category, keywords in CATEGORY_MAP.items():
        for keyword in keywords:
            if keyword in category_lower:
                return standard_category

    return category_lower



# Find the color of a product variant from its attributes list

def get_color(variant):
    
    # Loop through all attributes of the variant
    for attr in variant.get("attributes", []):
        
        # We only want the color attribute
        if attr.get("attribute_group", {}).get("slug") == "colors":
            return attr.get("value", "unknown")
    
    return "unknown"


def get_material(variant):

    #Extract material from variant attributes
    materials = []
    for attr in variant.get("attributes", []):
        if attr.get("attribute_group", {}).get("slug") == "materials":
            materials.append(attr.get("value", ""))
    return ", ".join(materials) if materials else "unknown"


# Find the dimensions (length, width, height) of a product variant
def get_size(variant):

    
    sizes = {} # empty dictionary to store sizes
    for size in variant.get("variant_sizes", []):

        sizes[size.get("type")] = size.get("value")  #"type" = length/width/height "value" = the actual number
    return sizes

# Find all Minimum Order Quantity based prices for a product variant
# e.g. buy 1-24 → 23.54 EUR, buy 25-49 → 22.93 EUR
def get_prices(variant):
    prices = []
    for price in variant.get("variant_prices", []):
        prices.append({
            "from_quantity": price.get("from_quantity", 1),  # minimum quantity
            "to_quantity": price.get("to_quantity", None), # maximum quantity
            "price": price.get("value", 0), # price per unit
            "currency": "EUR" # always EUR
        })
    return prices


def standardise_product(raw_product):
     
    # Extracting supplier and brand with fallback to 'unknown' to avoid null errors
    supplier = raw_product.get("supplier", {}).get("name", "unknown")
    brand = raw_product.get("brand", {}).get("name", "unknown")

    # Get category and normalise it
    # e.g "Razor" → "beauty"
    category_raw = raw_product.get("categories", [{}])[0].get("name", "unknown")
    category = normalise_category(category_raw)

    # Process each variant
    standardised_variants = []

    for variant in raw_product.get("variants", []):

        # Get color and normalise it
        # example "navy blue" → "blue"
        color_raw = get_color(variant)
        color = normalise_color(color_raw)

        # Text normalisation
        name = variant.get("name", "unknown").lower().strip()
        material = get_material(variant).lower().strip()

        # Size conversion
        size_mm = get_size(variant)
        size_cm = {key: round(value / 10, 2) for key, value in size_mm.items()} #API gives mm, we need cm, Logic: value / 10

        # Building the variant with required inventory fields (SKU, Price tiers, Stock)
        standardised_variant = {
            "sku":            variant.get("internal_reference", "unknown"),
            "supplier":       supplier.lower().strip(),
            "color":          color,
            "color_original": color_raw,
            "material":       material,
            "size_cm":        size_cm,      # converted to cm
            "price_tiers":    get_prices(variant),
            "stock":          variant.get("stock", 0),
            "in_stock":       variant.get("stock", 0) > 0
        }

        standardised_variants.append(standardised_variant)

    return standardised_variants

def transform_all(raw_products):

    print(f"Transforming {len(raw_products)} products")

    unified_products = []
    for product in raw_products:
        unified = standardise_product(product)
        unified_products.append(unified)

    print("Transformed Done!")
    return unified_products