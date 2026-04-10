from fastapi import FastAPI
import joblib
import numpy as np
from pydantic import BaseModel

app = FastAPI(title="Stock Price Prediction API",
    description="Predicts stock closing price using historical financial features",
    version="1.0")
model = joblib.load("model.joblib")
class InputData(BaseModel):
    Open: float
    High: float
    Low: float
    Volume: float
    Daily_Return: float
    Price_Range: float
    Price_Change: float
    Price_Change_Percent: float
    MA_7: float
    MA_30: float
    MA_90: float
    Volatility_7d: float

@app.get("/")
def root():
    return {"message": "ML API is running"}

@app.post("/predict")
def predict(data: InputData):
    features = np.array([[
        data.Open, data.High, data.Low, data.Volume,
        data.Daily_Return, data.Price_Range,
        data.Price_Change, data.Price_Change_Percent,
        data.MA_7, data.MA_30, data.MA_90,
        data.Volatility_7d
    ]])

    prediction = model.predict(features)
    return {
        "prediction": round(float(prediction[0]), 4),
        "status": "success"
    }


'''{
  "Open": 1.4,
  "High": 1.5,
  "Low": 1.3,
  "Volume": 5000000,
  "Daily_Return": 0.02,
  "Price_Range": 0.2,
  "Price_Change": 0.05,
  "Price_Change_Percent": 3.5,
  "MA_7": 1.3,
  "MA_30": 1.25,
  "MA_90": 1.2,
  "Volatility_7d": 0.03
}'''