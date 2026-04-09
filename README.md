# Full-Stack Machine Learning Architecture

## Overview
This repository contains a complete, ground-up implementation of a Machine Learning pipeline. It documents the journey from raw data management to a fully deployed predictive AI API, capped off with an interactive user interface.

## Tech Stack
* **Language:** Python, JavaScript, HTML/CSS
* **Data Processing:** Pandas
* **Visualization:** Matplotlib, Seaborn
* **Machine Learning:** Scikit-Learn (Linear Regression)
* **Backend API:** FastAPI, Uvicorn
* **Frontend UI:** Vanilla JS, DOM Manipulation, Fetch API

## Project Architecture
* **01_Python_Basics:** Memory optimization (Generators) and JSON File I/O.
* **02_Data_Structures:** Time-complexity optimized data mapping.
* **03_Kaggle_EDA:** Real-world CSV ingestion, missing data imputation, and statistical grouping.
* **04_Data_Visualization:** Translating Pandas DataFrames into visual business insights.
* **05_Machine_Learning:** Training a predictive model on real Zameen.com property data.
* **06_Real_Estate_API:** Freezing the trained model and serving it via a high-performance REST API with CORS middleware.
* **07_Real_Estate_Frontend:** An interactive, asynchronous web interface allowing users to query the AI and receive instant market valuations.

## How to Run Locally
1. Clone the repository.
2. Start the Backend API: `cd 06_Real_Estate_API` then run `uvicorn server:app --reload`
3. Launch the Frontend: Open `07_Real_Estate_Frontend/index.html` in any modern web browser.