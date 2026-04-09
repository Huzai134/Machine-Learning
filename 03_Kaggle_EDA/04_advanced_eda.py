import pandas as pd

# Loading the dummy CSV dataset we made earlier
file_path = "03_Kaggle_EDA/pakistan_real_estate.csv"
df = pd.read_csv(file_path)

print("--- 1. FILTERING ---")
# I only want to see properties that are actually on the market (Active)
active_listings = df[df["Status"] == "Active"]

print("Just the active ones:")
# Using double brackets to only print the columns I actually care about
print(active_listings[["City", "Property_Type", "Price_PKR"]])
print("\n")


print("--- 2. GROUPING ---")
# This is the magic line. Grouping by city to see where the expensive stuff is.
avg_price_by_city = df.groupby("City")["Price_PKR"].mean()

print("Average price in each city:")
# Using a quick lambda function to format the numbers like actual money
print(avg_price_by_city.apply(lambda x: f"{x:,.0f} PKR"))
print("\n")


print("--- 3. SORTING ---")
# Finding the top 2 most expensive properties in the whole dataset
# ascending=False puts the biggest numbers at the top
most_expensive = df.sort_values(by="Price_PKR", ascending=False).head(2)

print("Top 2 most expensive properties overall:")
print(most_expensive[["City", "Property_Type", "Price_PKR"]])