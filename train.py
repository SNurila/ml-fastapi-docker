import pandas as pd
import numpy as np
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error
import joblib

df = pd.read_csv("tesla_stock_data_2010_2025.csv")
df = df.dropna()

features = [
    "Open", "High", "Low", "Volume",
    "Daily_Return", "Price_Range",
    "Price_Change", "Price_Change_Percent",
    "MA_7", "MA_30", "MA_90",
    "Volatility_7d"
]

X = df[features]
y = df["Close"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

mlflow.set_experiment("stock_prediction")

with mlflow.start_run():
    model = RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    mlflow.log_param("model_type", "RandomForest")
    mlflow.log_param("n_estimators", 100)
    mlflow.log_param("max_depth", 10)
    mlflow.log_param("test_size", 0.2)
    mlflow.log_param("random_state", 42)

    r2   = model.score(X_test, y_test)
    rmse = mean_squared_error(y_test, y_pred) ** 0.5
    mae  = mean_absolute_error(y_test, y_pred)

    mlflow.log_metric("r2_score", r2)
    mlflow.log_metric("rmse", rmse)
    mlflow.log_metric("mae", mae)

    mlflow.sklearn.log_model(
        model,
        artifact_path="model",
        registered_model_name="StockPriceModel"   # ← this covers Model Registry requirement
    )

    joblib.dump(model, "model.joblib")

    print(f"Done! R²={r2:.4f} | RMSE={rmse:.4f} | MAE={mae:.4f}")
    print("Model registered in MLflow as 'StockPriceModel'")