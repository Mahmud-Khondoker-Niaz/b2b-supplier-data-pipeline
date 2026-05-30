# test.py
import json

with open('output/unified_catalogue.json', 'r') as f:
    data = json.load(f)

# Check category and variants structure
print("Category:", data[0]['category'])
print("Supplier:", data[0]['supplier'])
print("\nVariants type:", type(data[0]['variants']))
print("\nFirst variant type:", type(data[0]['variants'][0]))
print("\nFirst variant:")
print(json.dumps(data[0]['variants'][0], indent=2)[:300])