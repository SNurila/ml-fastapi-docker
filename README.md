# Stock Price Prediction API

This project is a containerized Machine Learning API built with FastAPI. It uses a Random Forest Regressor trained on Tesla stock data (2010–2025) to predict the closing price of a stock based on various financial indicators.

Project Structure
* `train.py`: Jupyter notebook/script to train and save the ML model.
* `main.py`: The FastAPI application that serves predictions.
* `model.joblib`: The serialized (saved) trained model.
* `requirements.txt`: List of Python dependencies (FastAPI, Scikit-learn, etc.).
* `Dockerfile`: Instructions to containerize the application.

---

Local Setup (Without Docker)

1. Install dependencies:
   ```bash
   pip install -r requirements.txt