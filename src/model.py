import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.ensemble import VotingRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.preprocessing import StandardScaler
import shap
import matplotlib.pyplot as plt
import seaborn as sns

def prepare_data(data_421, data_422):
    """Prepare dataset with engineered features for viscosity prediction"""
    data_combined_1 = pd.DataFrame(data_421)
    data_combined_2 = pd.DataFrame(data_422)
    data_combined_1["Dataset"] = "Table 4.2.1"
    data_combined_2["Dataset"] = "Table 4.2.2"
    data_combined = pd.concat([data_combined_1, data_combined_2], ignore_index=True)
    
    # Physical properties and engineered features
    data_combined["Density"] = 0.95
    data_combined["Temperature"] = np.linspace(60, 977, len(data_combined))
    data_combined["Shear_Stress_Rate_Ratio"] = data_combined["Shear Stress"] / (data_combined["Shear Rate"] + 1e-6)
    data_combined["Temperature_Density_Product"] = data_combined["Temperature"] * data_combined["Density"]
    
    return data_combined

def create_ensemble_model():
    """Create ensemble model with Decision Tree, Linear Regression, and KNN"""
    dt_model = DecisionTreeRegressor(random_state=42)
    lr_model = LinearRegression()
    knn_model = KNeighborsRegressor(n_neighbors=3)
    
    ensemble = VotingRegressor(estimators=[
        ('dt', dt_model),
        ('lr', lr_model),
        ('knn', knn_model)
    ])
    
    return ensemble, dt_model

def analyze_model_performance(model, X_train, X_test, y_train, y_test, feature_names):
    """Analyze individual model contributions and overall ensemble performance"""
    # Train individual models
    models = {
        'Decision Tree': DecisionTreeRegressor(random_state=42),
        'Linear Regression': LinearRegression(),
        'KNN': KNeighborsRegressor(n_neighbors=3)
    }
    
    results = {}
    for name, m in models.items():
        m.fit(X_train, y_train)
        y_pred = m.predict(X_test)
        results[name] = {
            'r2': r2_score(y_test, y_pred),
            'rmse': np.sqrt(mean_squared_error(y_test, y_pred))
        }
    
    return results