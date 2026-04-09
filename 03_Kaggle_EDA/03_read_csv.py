"""
TOPIC: Reading External CSV Files
GOAL: Load a raw .csv file from the hard drive into Pandas and use 
professional EDA commands to instantly understand the dataset.
"""

import pandas as pd

# 1. LOAD THE FILE
# This command reads the CSV and converts it into a DataFrame
file_path = "03_Kaggle_EDA/pakistan_real_estate.csv"
df = pd.read_csv(file_path)

print("--- 1. PEEK AT THE DATA ---")
# .head() shows ONLY the first 5 rows. 
# CRITICAL: If you load 1 million rows, printing 'df' will crash your terminal. 
# ALWAYS use .head() to just peek at the top.
print(df.head())
print("\n")

print("--- 2. INSTANT TECHNICAL SUMMARY ---")
# .info() tells you exactly how many columns you have, their data types, 
# and instantly spots missing (null) values.
print(df.info())
print("\n")

print("--- 3. INSTANT STATISTICAL ANALYSIS ---")
# .describe() automatically finds all numeric columns and calculates 
# the count, mean, standard deviation, min, and max in one millisecond.
print(df.describe())