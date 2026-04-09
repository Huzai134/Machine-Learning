"""
TOPIC: Introduction to Pandas (DataFrames)

THE PROBLEM: 
Standard Python dictionaries and 'for' loops are too slow to process 
massive datasets (e.g., 500,000+ rows). Doing complex math on them 
requires writing highly inefficient code.

THE SOLUTION:
The Pandas library converts raw data into a highly optimized 2D table 
called a DataFrame. Because it is powered by C under the hood, we can 
perform Exploratory Data Analysis (EDA) like filtering and finding averages 
instantly with single-line commands.
"""

import pandas as pd

# 1. THE RAW DATA
car_data = {
    "Brand": ["Toyota", "Suzuki", "Honda", "KIA", "Suzuki"],
    "Model": ["Corolla", "Alto", "Civic", "Sportage", "Cultus"],
    "Price_PKR": [4500000, 2200000, 8500000, 7300000, 3800000],
    "Units_Sold": [45000, 82000, 18000, 25000, 40000]
}

# 2. CREATE THE DATAFRAME
df = pd.DataFrame(car_data)

print("--- 1. THE RAW DATAFRAME ---")
print(df)
print("\n")

# 3. INSTANT EXPLORATORY DATA ANALYSIS (EDA)
print("--- 2. BASIC EDA ---")
avg_price = df["Price_PKR"].mean()
total_sales = df["Units_Sold"].sum()

print(f"Average Car Price: {avg_price:,.0f} PKR")
print(f"Total Cars Sold: {total_sales:,}")

# 4. INSTANT FILTERING
print("\n--- 3. FILTERED DATA (Suzuki Only) ---")
suzuki_only = df[df["Brand"] == "Suzuki"]
print(suzuki_only)