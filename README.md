# 🚀 Full-Stack Machine Learning & AI Portfolio

A collection of end-to-end AI and Machine Learning applications covering the entire software lifecycle: from data engineering and model training to third-party LLM integration, secure cloud deployment, and custom front-end interfaces.

---

## 🛠️ Project 1: Twin Cities Real Estate AI Engine
A complete Machine Learning pipeline designed to predict property prices in Islamabad/Rawalpindi using real-world market data. 

* **Live API Endpoint:** [https://machine-learning-al2p.onrender.com/docs](https://machine-learning-al2p.onrender.com/docs)
* **Tech Stack:** Python, Scikit-Learn (Linear Regression), Pandas, FastAPI, HTML/JS.
* **Architecture Highlights:**
    * **Data Engineering:** Ingested and cleaned 100k+ rows of local real estate data, handling outliers and feature engineering.
    * **Model Training:** Mapped `Area_Marla` and `Bedrooms` to market valuation, serialized as a `.pkl` file.
    * **Cloud API:** Robust FastAPI backend with CORS middleware for secure cross-origin requests.

---

## 📝 Project 2: AI Cover Letter Generator (Micro-SaaS)
An AI-powered web tool that acts as an expert technical recruiter, generating highly tailored cover letters by cross-referencing a user's resume with a specific job description.

* **Live Web App:** [https://Huzai134.github.io/Machine-Learning/08_AI_Cover_Letter/index.html](https://Huzai134.github.io/Machine-Learning/08_AI_Cover_Letter/index.html)
* **Live API Endpoint:** [https://machine-learning-2-iri6.onrender.com/docs](https://machine-learning-2-iri6.onrender.com/docs)
* **Tech Stack:** Google Gemini 2.0 Flash API, Python, FastAPI, GitHub Pages.
* **Architecture Highlights:**
    * **LLM Integration:** Built a secure bridge to Google's Gemini models using modern SDKs.
    * **Prompt Engineering:** Engineered strict system instructions to enforce professional formatting and dynamic data injection.
    * **Security:** Safely managed environment variables (`.env`) to protect private API keys during Render cloud deployment.

------
## 🚀 How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/Huzai134/Machine-Learning.git
cd Machine-Learning
```

### 2. Set up the Backend (Example: Cover Letter API)
```bash
cd 08_AI_Cover_Letter
pip install -r requirements.txt
uvicorn server:app --reload
```

## 👨‍💻 About the Developer

Muhammad Huzaifa Farooqui | Computer Science (BSCS '27) @ National University of Modern Languages (NUML)

I specialize in building bridges between complex back-end logic and user-friendly interfaces. Currently focused on Machine Learning architectures, Full-Stack Web Development, and API integrations.

GitHub: https://github.com/Huzai134