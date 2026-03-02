# 💤 Sleep Quality Prediction API

A Machine Learning powered REST API built using FastAPI to predict sleep quality based on lifestyle and health metrics.

---

## 🚀 Project Overview

This project uses a trained Scikit-Learn model to predict sleep quality based on:

- Gender
- Age
- Occupation
- Sleep Duration
- Physical Activity Level
- Stress Level
- BMI Category
- Heart Rate
- Daily Steps
- Blood Pressure (Systolic & Diastolic)

The model was trained using scikit-learn (v1.6.1) and deployed using FastAPI.

---

## 🛠 Tech Stack

- Python 3.10
- FastAPI
- Uvicorn
- Scikit-learn 1.6.1
- Pandas
- Joblib

---

## 📦 Installation

### 1️⃣ Clone the repository


pip install -r requirements.txt


### 

```bash
git clone <your-repo-link>
cd sleep_quality

run app: 

uvicorn main:app

