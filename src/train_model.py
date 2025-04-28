# scripts/train_model.py

import pandas as pd
import numpy as np
import os
import joblib
import yaml
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# --- Define ROOT PATH automatically ---
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# --- Set paths dynamically ---
CONFIG_PATH = os.path.join(ROOT_DIR, "config", "train_config.yaml")

# --- Load configuration ---
if not os.path.exists(CONFIG_PATH):
    raise FileNotFoundError(f"Config file not found at {CONFIG_PATH}")

with open(CONFIG_PATH, "r") as f:
    config = yaml.safe_load(f)

# Resolve paths from config
data_path = os.path.join(ROOT_DIR, config["data_path"])
output_dir = os.path.join(ROOT_DIR, config["model_output_dir"])
model_filename = config["model_filename"]

# --- Load dataset ---
if not os.path.exists(data_path):
    raise FileNotFoundError(f"Dataset not found at {data_path}")

df = pd.read_csv(data_path)

# --- Prepare features and target ---
TARGET_COLUMN = "viscosity"  # You can also put this in config later if needed

X = df.drop(columns=[TARGET_COLUMN])
y = df[TARGET_COLUMN]

# --- Split into training and test sets ---
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=config["test_size"],
    random_state=config["random_state"]
)

# --- Define and train the model ---
model = RandomForestRegressor(
    n_estimators=config["n_estimators"],
    max_depth=config["max_depth"],
    random_state=config["random_state"],
    n_jobs=config["n_jobs"]
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
os.makedirs(output_dir, exist_ok=True)
model_path = os.path.join(output_dir, model_filename)
joblib.dump(model, model_path)

print(f"Trained model saved to {model_path}")
