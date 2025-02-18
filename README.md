# Heavy Oil Rheology Machine Learning

## Research Overview

This research presents an innovative machine learning approach to analyze flow properties of heavy crude oil under thermal conditions, focusing on the Agbabu bitumen deposit in Ondo State, Nigeria.

## 🚀 Features

- Advanced data preprocessing for rheological data
- Machine learning pipeline with Gradient Boosting Regressor
- Predictive modeling for:
  - Apparent Viscosity
  - Plastic Viscosity
  - Yield Point
- SHAP (SHapley Additive exPlanations) feature importance analysis
- Performance metrics visualization
- Flexible and extensible machine learning workflow

## 📦 Installation

### Prerequisites
- Python 3.8+
- pip package manager

### Install from GitHub
```bash
git clone https://github.com/ol-s-cloud/heavy-oil-rheology-ml.git
cd heavy-oil-rheology-ml
pip install -r requirements.txt
```

### Install as a Package
```bash
pip install git+https://github.com/ol-s-cloud/heavy-oil-rheology-ml.git
```

## 🔍 Usage

### Basic Analysis
```python
from heavy_oil_ml.pipeline import run_analysis

# Run complete analysis
results = run_analysis()
```

### Advanced Usage
```python
from heavy_oil_ml.pipeline import run_analysis
from heavy_oil_ml.visualization import plot_actual_vs_predicted, plot_shap_values

# Run analysis
results = run_analysis()

# Visualize results for each target variable
for target, result in results.items():
    # Plot actual vs predicted values
    plot_actual_vs_predicted(
        y_test=result['y_test'], 
        y_pred=result['y_pred'], 
        target_name=target
    )
    
    # Plot SHAP feature importance
    plot_shap_values(
        shap_values=result['shap_values'], 
        feature_names=result['poly_feature_names'], 
        target_name=target
    )
```

## Machine Learning Pipeline Architecture

![ML Pipeline Architecture](research_paper/ml_pipeline_architecture.png)

## Performance Metrics Visualization

![Rheology Metrics Visualization](research_paper/rheology_metrics_visualization.png)

## Performance Metrics

### Yield Point Prediction
- R² Score: 0.9627
- RMSE: 30.5390 Pa
- MAE: 27.7179 Pa

### Apparent Viscosity Prediction
- R² Score: 0.8428
- RMSE: 2.1546 Pa·s
- MAE: 1.6650 Pa·s

## Experimental Device

### Haake RS 6000 Rheometer

![Haake RS 6000 Rheometer](research_paper/haake_rs6000_rheometer.jpg)

[Rest of the previous README content remains the same]