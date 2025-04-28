# scripts/train_model.py

import pandas as pd
import numpy as np
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# --- Load dataset ---
DATA_PATH = "data/dataset.csv"  # Adjust if your dataset path is different

if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(f"Dataset not found at {DATA_PATH}")

df = pd.read_csv(DATA_PATH)

# --- Prepare features and target ---
TARGET_COLUMN = "viscosity"  # Adjust if your target variable has a different name

X = df.drop(columns=[TARGET_COLUMN])
y = df[TARGET_COLUMN]

# --- Split into training and test sets ---
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- Define and train the model ---
model = RandomForestRegressor(
    n_estimators=100,
    max_depth=None,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

# --- Evaluate the model ---
y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Model Evaluation:")
print(f" - MAE: {mae:.4f}")
print(f" - MSE: {mse:.4f}")
print(f" - R2 Score: {r2:.4f}")

# --- Save the model ---
OUTPUT_DIR = "models"
os.makedirs(OUTPUT_DIR, exist_ok=True)

MODEL_PATH = os.path.join(OUTPUT_DIR, "random_forest_model.pkl")
joblib.dump(model, MODEL_PATH)

print(f"Trained model saved to {MODEL_PATH}")
