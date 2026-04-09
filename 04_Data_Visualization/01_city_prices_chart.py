import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. LOAD THE DATA 
# (We are borrowing the CSV from the previous folder)
file_path = "03_Kaggle_EDA/pakistan_real_estate.csv"
df = pd.read_csv(file_path)

# 2. PREPARE THE DATA
# Grouping by city just like we did in the last lesson
avg_price_by_city = df.groupby("City")["Price_PKR"].mean().reset_index()

# 3. CONFIGURE THE VISUALS
# Seaborn makes things look modern instead of like Windows 95
sns.set_theme(style="whitegrid")

# Create a blank canvas (width: 8, height: 6)
plt.figure(figsize=(8, 6))

# 4. DRAW THE CHART
# x = what goes on the bottom, y = what goes on the side, data = our grouped numbers
sns.barplot(x="City", y="Price_PKR", data=avg_price_by_city, palette="viridis")

# 5. ADD LABELS AND TITLE
plt.title("Average Property Price by City (PKR)", fontsize=16)
plt.xlabel("City", fontsize=12)
plt.ylabel("Average Price (Tens of Millions)", fontsize=12)

# Prevent the labels from getting cut off at the edges
plt.tight_layout()

# 6. SHOW IT TO THE USER
# This line physically opens a new window on your computer to show the graph
plt.show()