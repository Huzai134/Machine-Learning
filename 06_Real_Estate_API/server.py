from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  
from pydantic import BaseModel
import joblib
import pandas as pd

# 1. Start the API app
app = FastAPI(title="Twin Cities Real Estate AI API")


# Tell the server to accept requests from our HTML file -->
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows any website to connect
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# The ../ tells Linux to go UP one folder to find the ML files
model = joblib.load("../05_Machine_Learning/real_estate_model.pkl")

# 3. Define what a "House" looks like so the API knows what data to expect
class House(BaseModel):
    area_marla: float
    bedrooms: int

# 4. Create the URL endpoint that the frontend will talk to
@app.post("/predict")
def predict_price(house: House):
    # Convert the internet JSON request into a Pandas table for the AI
    ai_input = pd.DataFrame({"Area_Marla": [house.area_marla], "Bedrooms": [house.bedrooms]})
    
    # Ask the AI to guess the price based on current market trends
    prediction = model.predict(ai_input)[0]
    
    # Send the answer back to the internet
    return {
        "status": "success",
        "house_details": house,
        "predicted_price_pkr": round(prediction)
    }

# A simple welcome page just to check if the server is online
@app.get("/")
def home():
    return {"message": "Welcome to the Twin Cities Real Estate AI API! The server is running."}