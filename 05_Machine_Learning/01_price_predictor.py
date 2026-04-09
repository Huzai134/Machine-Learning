import pandas as pd
from sklearn.linear_model import LinearRegression

print("--- 1. LOADING DATA ---")
# 1. Get our historical data
file_path = "03_Kaggle_EDA/pakistan_real_estate.csv"
df = pd.read_csv(file_path)

# Drop any rows with missing data so our AI doesn't get confused
df = df.dropna()
print("Data loaded and cleaned successfully.\n")


print("--- 2. TRAINING THE AI ---")
# X = The "Features" (What the AI uses to make a guess)
# Y = The "Target" (The actual answer we want the AI to learn)
X = df[["Area_Marla", "Bedrooms"]] 
y = df["Price_PKR"]

# 'Hire' the Machine Learning Model (Linear Regression)
ai_model = LinearRegression()

# .fit() is the magic word. This line forces the AI to study the historical data 
# and figure out exactly how much 1 Marla and 1 Bedroom adds to the total price.
ai_model.fit(X, y)
print("Model training complete! The AI has learned the market patterns.\n")


print("--- 3. PREDICTING THE FUTURE ---")
# A client asks: "How much for a 15-Marla house with 3 Bedrooms?"
# We format their question exactly like our 'X' data
new_house = pd.DataFrame({"Area_Marla": [15], "Bedrooms": [3]})

# .predict() asks the AI to guess the price based on what it learned
predicted_price = ai_model.predict(new_house)

print(f"Client House Details: 15 Marla, 3 Bedrooms")
print(f"AI Recommended Price: {predicted_price[0]:,.0f} PKR")