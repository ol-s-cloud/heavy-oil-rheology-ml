import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import shap
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

from .data_preparation import prepare_data

def create_model_pipeline():
    """
    Create a pipeline with data preprocessing and a Gradient Boosting Regressor.

    Returns:
        sklearn.pipeline.Pipeline: Configured pipeline object.
    """
    gb_regressor = GradientBoostingRegressor(
        n_estimators=100,  # Number of trees
        learning_rate=0.1,  # Step size for optimization
        max_depth=3,  # Maximum depth of each tree
        random_state=42  # Random seed for reproducibility
    )

    pipeline = Pipeline([
        ('scaler', StandardScaler()),  # Standardize features by removing mean and scaling to unit variance
        ('poly', PolynomialFeatures(degree=2, include_bias=False)),  # Add polynomial interaction terms
        ('regressor', gb_regressor)  # Gradient Boosting Regressor as the model
    ])

    return pipeline

def evaluate_model(model, X_train, X_test, y_train, y_test, feature_names, target_name):
    """
    Train the model, evaluate performance, and visualize results.

    Args:
        model (Pipeline): The machine learning pipeline.
        X_train (pd.DataFrame): Training features.
        X_test (pd.DataFrame): Testing features.
        y_train (pd.Series): Training target.
        y_test (pd.Series): Testing target.
        feature_names (list): List of original feature names.
        target_name (str): Name of the target variable.

    Returns:
        dict: Evaluation metrics and trained model.
    """
    # Train the model
    model.fit(X_train, y_train)

    # Predict on test data
    y_pred = model.predict(X_test)

    # Compute evaluation metrics
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)

    # Get feature names after polynomial transformation
    poly_feature_names = model.named_steps['poly'].get_feature_names_out(feature_names)

    # SHAP feature importance analysis
    explainer = shap.TreeExplainer(model.named_steps['regressor'])
    shap_values = explainer.shap_values(model.named_steps['poly'].transform(
        model.named_steps['scaler'].transform(X_test)))

    return {
        'mse': mse,
        'rmse': rmse,
        'r2': r2,
        'mae': mae,
        'model': model,
        'shap_values': shap_values,
        'poly_feature_names': poly_feature_names
    }

def run_analysis(verbose=True):
    """
    Run complete analysis on dataset.

    Args:
        verbose (bool): Whether to print detailed results.

    Returns:
        dict: Results for each target variable.
    """
    # Prepare the dataset
    data_combined = prepare_data()

    # Define features and target variables
    features = ["Density", "Temperature", "Shear Stress", "Shear Rate",
                "Shear_Stress_Rate_Ratio", "Temperature_Density_Product"]
    targets = ["Apparent Viscosity", "Plastic Viscosity", "Yield Point"]

    # Dictionary to store results for each target variable
    results = {}

    # Loop through each target variable
    for target in targets:
        if verbose:
            print(f"\nModeling for {target}")

        # Split data into training and testing sets
        X = data_combined[features]
        y = data_combined[target]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Create and evaluate the model pipeline
        model = create_model_pipeline()
        result = evaluate_model(model, X_train, X_test, y_train, y_test, features, target)
        results[target] = result

        if verbose:
            print(f"RMSE: {result['rmse']:.4f}")
            print(f"R2 Score: {result['r2']:.4f}")
            print(f"MAE: {result['mae']:.4f}")

    return results