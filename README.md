# 🚀 Full-Stack Real Estate AI Prediction Engine

A complete end-to-end Machine Learning solution designed to predict property prices in the Twin Cities (Islamabad/Rawalpindi) using real-world market data. This project covers the entire software lifecycle: from raw data cleaning and model training to cloud-hosted API deployment and a custom web interface.

---

## 🔗 Live Demo & Links
* **Live API Endpoint:** [https://machine-learning-al2p.onrender.com](https://machine-learning-al2p.onrender.com)
* **Interactive UI:** Open `07_Real_Estate_Frontend/index.html` locally to query the live cloud model.
* **API Documentation:** [https://machine-learning-al2p.onrender.com/docs](https://machine-learning-al2p.onrender.com/docs)

---

## 🛠️ Tech Stack
* **Language:** Python 3.14+, JavaScript, HTML5, CSS3
* **Machine Learning:** Scikit-Learn (Linear Regression), Joblib
* **Data Science:** Pandas, NumPy, Matplotlib, Seaborn
* **Backend:** FastAPI (High-performance Python framework), Uvicorn
* **Cloud DevOps:** Render (Deployment), GitHub Actions (CI/CD)

---

## 🏗️ Project Architecture

The project is organized into a modular pipeline to ensure scalability and professional organization:

* **01-02_Python_Core:** Foundational logic, memory-efficient generators, and optimized data structures.
* **03_Data_Engineering:** Ingesting 100k+ rows of Pakistan Real Estate data. Handled missing values, outliers, and feature engineering.
* **04_Exploratory_Data_Analysis:** Statistical visualization of price trends across different cities and property types.
* **05_Machine_Learning:** Training a predictive model. Used Scikit-Learn to map `Area_Marla` and `Bedrooms` to market valuation. The model is "frozen" as a `.pkl` file for production.
* **06_Cloud_API:** A robust FastAPI server that loads the AI "brain" and serves predictions via JSON. Includes **CORS middleware** to allow secure cross-origin web requests.
* **07_Interactive_Frontend:** A sleek, modern web UI that allows users to get instant AI-generated valuations without touching a single line of code.

---

## 🚀 How to Run Locally

### 1. Clone the repository
```bash
git clone [https://github.com/Huzai134/Machine-Learning.git](https://github.com/Huzai134/Machine-Learning.git)
cd Machine-Learning