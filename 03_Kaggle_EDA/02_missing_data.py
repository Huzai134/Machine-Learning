"""
TOPIC: Handling Missing Data in Pandas

THE PROBLEM: 
Real-world Kaggle datasets are never perfect. They contain empty cells 
due to human error or broken sensors. If fed directly into a Machine Learning 
model, these empty values (NaN) will cause the algorithm to crash.

THE SOLUTION:
Pandas provides built-in tools to detect missing data (.isnull().sum()) 
and offers distinct strategies to handle it: either deleting the corrupted 
rows completely (.dropna()) or intelligently filling the holes with 
calculated averages (.fillna()).
"""

import pandas as pd

# 1. THE MESSY DATA ('None' creates empty holes)
messy_data = {
    "Brand": ["Toyota", "Suzuki", "Honda", "KIA", "Hyundai"],
    "Model": ["Corolla", "Alto", "Civic", None, "Tucson"],
    "Price_PKR": [4500000, 2200000, None, 7300000, 8000000],
    "Units_Sold": [45000, 82000, 18000, 25000, None]
}

df = pd.DataFrame(messy_data)

print("--- 1. DETECTING MISSING VALUES (NaN) ---")
print(df.isnull().sum())
print("\n")

# 2. STRATEGY A: Drop the corrupted rows
print("--- 2. CLEANING: Dropping Rows ---")
df_dropped = df.dropna()
print(df_dropped)
print("\n")

# 3. STRATEGY B: Fill the holes (Data Imputation)
print("--- 3. CLEANING: Filling with Averages ---")
# Calculate the average price of the cars we DO have
average_price = df["Price_PKR"].mean()

# Plug that average price into the empty Honda slot to save the row
df_filled = df.copy()
df_filled["Price_PKR"] = df_filled["Price_PKR"].fillna(average_price)

print(df_filled)