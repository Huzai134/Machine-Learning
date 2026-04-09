# Full-Stack Machine Learning Architecture

## Overview
This repository contains a complete, ground-up implementation of a Machine Learning pipeline. It documents the journey from raw data management to a fully deployed predictive AI API. 

## Tech Stack
* **Language:** Python
* **Data Processing:** Pandas
* **Visualization:** Matplotlib, Seaborn
* **Machine Learning:** Scikit-Learn (Linear Regression)
* **Backend API:** FastAPI, Uvicorn

## Project Architecture
* **01_Python_Basics:** Memory optimization (Generators) and JSON File I/O.
* **02_Data_Structures:** Time-complexity optimized data mapping.
* **03_Kaggle_EDA:** Real-world CSV ingestion, missing data imputation, and statistical grouping.
* **04_Data_Visualization:** Translating Pandas DataFrames into visual business insights.
* **05_Machine_Learning:** Training a predictive model on real Zameen.com property data.
* **06_Real_Estate_API:** Freezing the trained model and serving it via a high-performance REST API.

## How to Run the API
1. Clone the repository.
2. Navigate to the API directory: `cd 06_Real_Estate_API`
3. Launch the server: `uvicorn server:app --reload`
4. Access the interactive testing environment at `http://127.0.0.1:8000/docs`