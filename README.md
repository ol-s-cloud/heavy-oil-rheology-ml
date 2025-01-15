# Bitumen Rheology Modeling and Machine Learning Pipeline

This project aims to model the rheological properties of natural bitumen using machine learning techniques. The focus is on predicting viscosity characteristics such as apparent viscosity, plastic viscosity, and yield point based on various input parameters, including shear stress, shear rate, temperature, and density. The machine learning pipeline includes data preprocessing, feature engineering, and regression analysis using a Gradient Boosting Regressor (GBR).

## Features

- **Data Preparation**: Combines multiple data tables for modeling and feature engineering.
- **Machine Learning Pipeline**: Uses a Gradient Boosting Regressor (GBR) model to predict key rheological properties of natural bitumen.
- **Polynomial Feature Expansion**: Applies polynomial feature transformation for better modeling of non-linear relationships.
- **SHAP (SHapley Additive exPlanations)**: Visualizes feature importance and provides model interpretability.
- **Evaluation Metrics**: Computes evaluation metrics such as RMSE, R², and MAE for model assessment.
- **Visualization**: Includes plots for actual vs predicted values, as well as SHAP summary plots for feature importance.

## Project Setup

### Prerequisites

Make sure you have Python 3.x and the necessary libraries installed. You can install the required packages by running:

```bash
pip install pandas numpy scikit-learn matplotlib shap
