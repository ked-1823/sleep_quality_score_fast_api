from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import pandas as pd

model = joblib.load('sleep_quality_model.pkl')

app = FastAPI()

# ✅ ADD THIS BLOCK HERE
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow frontend to access
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SleepData(BaseModel):
    Gender: str
    Age: int
    Occupation: str
    Sleep_Duration: float
    Physical_Activity_Level: int
    Stress_Level: int
    BMI_Category: str
    Heart_Rate: int
    Daily_Steps: int
    Systolic_BP: int
    Diastolic_BP: int


@app.get("/")
def home():
    return {"message": "Welcome to the Sleep Quality Prediction API!"}


@app.post("/predict")
def predict(data: SleepData):

    input_df = pd.DataFrame([{
        "Gender": data.Gender,
        "Age": data.Age,
        "Occupation": data.Occupation,
        "Sleep Duration": data.Sleep_Duration,
        "Physical Activity Level": data.Physical_Activity_Level,
        "Stress Level": data.Stress_Level,
        "BMI Category": data.BMI_Category,
        "Heart Rate": data.Heart_Rate,
        "Daily Steps": data.Daily_Steps,
        "Systolic_BP": data.Systolic_BP,
        "Diastolic_BP": data.Diastolic_BP
    }])

    prediction = model.predict(input_df)

    return {"predicted_sleep_quality": prediction[0]}