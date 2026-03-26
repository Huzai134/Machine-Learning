"""
GOAL: Data Cleaning & Relationship Mapping
TOOLS: Sets (for uniqueness) and Dictionaries (for O(1) lookups).
USE CASE: Identifying unsupported or 'outlier' data points in a 
raw dataset without using slow nested loops.
"""
# Raw, "dirty" data from a mock car sales API
raw_brands = ["Toyota", "Suzuki", "Honda", "Suzuki", "Toyota", "KIA", "Honda", "Suzuki"]

# 1. SETS: Remove all duplicates in one step
unique_brands = set(raw_brands)
print(f"Unique Brands: {unique_brands}")

# 2. DICTIONARIES: Mapping relationships
# Let's map these brands to their Country of Origin
brand_origin = {
    "Toyota": "Japan",
    "Suzuki": "Japan",
    "Honda": "Japan",
    "KIA": "South Korea",
    "Mercedes": "Germany"
}

# 3. FAST LOOKUP: Finding the origin of a brand
# Instead of a loop, we go straight to the key
search_brand = "KIA"
if search_brand in brand_origin:
    print(f"{search_brand} is from {brand_origin[search_brand]}")

# 4. SET OPERATIONS: Comparing two datasets
# Brands we have vs. Brands we want to support
supported_brands = {"Toyota", "Honda", "KIA", "Hyundai","Mercedes"}
available_brands = set(raw_brands)

# Find brands we have that are NOT supported (Difference)
unsupported = available_brands - supported_brands
print(f"Unsupported brands found: {unsupported}")