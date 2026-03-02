from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd


model=joblib.load('sleep_quality_model.pkl')  #loaded the trained model

app = FastAPI() #created an instance of FastAPI

class SleepData(BaseModel): #defined a Pydantic model to validate the input data
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

@app.get("/") #defined a root endpoint
def home():
    return {"message": "Welcome to the Sleep Quality Prediction API!"}

@app.post("/predict") #defined a POST endpoint for making predictions
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
    prediction=model.predict(input_df)  #used the loaded model to make a prediction
    return {"predicted_sleep_quality": prediction[0]}  #returned the predicted sleep quality        