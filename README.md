### Heavy Oil Rheological Properties Analysis using Ensemble Machine Learning

## Overview
This repository contains a machine learning analysis of heavy crude oil rheological properties using an ensemble approach combining Decision Trees, Linear Regression, and K-Nearest Neighbors (KNN). The analysis focuses on predicting and understanding various viscosity parameters and their relationships with temperature and shear conditions.

## Features
- Ensemble model combining:
  - Decision Tree Regression
  - Linear Regression
  - K-Nearest Neighbors (KNN)
- SHAP (SHapley Additive exPlanations) analysis for model interpretation
- Cross-validation for model performance evaluation
- Feature importance analysis

## Data Parameters
The analysis includes the following key parameters:
1. Independent Variables:
   - Density
   - Temperature
   - Shear Stress
   - Shear Rate

2. Target Variables:
   - Apparent Viscosity
   - Plastic Viscosity
   - Yield Point

## Model Components
1. Data Preparation:
   - Feature scaling using StandardScaler
   - Train-test splitting
   - Data combination from multiple experimental sources

2. Model Pipeline:
   - Ensemble voting regressor
   - Cross-validation scoring
   - Feature importance ranking

3. Analysis Tools:
   - SHAP value calculations
   - Performance metrics (RMSE, R², MAE)
   - Feature interaction analysis

## Requirements
```python
pandas
numpy
scikit-learn
shap
matplotlib
seaborn
```

## Usage
```python
# Example usage of the model
from model import create_ensemble_model, evaluate_model

# Prepare your data
X = your_feature_data
y = your_target_variable

# Create and evaluate model
model = create_ensemble_model()
results = evaluate_model(X_train, X_test, y_train, y_test, feature_names, target_name)
```

## Model Performance
The ensemble model provides:
- Comprehensive viscosity predictions
- Feature importance rankings
- Cross-validated performance metrics
- SHAP-based interpretability

## License
MIT License

## Future Improvements
1. Model Enhancements:
   - Gradient Boosting implementation
   - Deep learning integration
   - Advanced error analysis

2. Feature Engineering:
   - Additional interaction terms
   - Temperature-dependent features
   - Non-linear transformations

3. Analysis Extensions:
   - Uncertainty quantification
   - Real-time prediction capabilities
   - Extended cross-validation studies

## Contact
For questions or feedback, please open an issue in the repository.