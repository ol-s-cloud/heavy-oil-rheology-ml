# Machine Learning Analysis of Heavy Crude Oil Rheological Properties: A Case Study of the Eastern Dahomey Basin, Nigeria

## Overview
This repository contains a machine learning-based analysis of heavy crude oil rheological properties from Nigeria's Eastern Dahomey Basin. The study focuses on understanding and predicting various viscosity parameters using an ensemble learning approach, with particular emphasis on the effects of temperature and shear conditions on flow properties.

## Research Context
The Eastern Dahomey Basin in Southwest Nigeria contains significant heavy crude oil deposits that present extraction challenges due to high viscosity. This study investigates:
- Flow properties under various conditions
- Rheological parameters with biosolvent dilution
- Temperature-dependent viscosity behavior
- Shear stress/rate relationships

## Key Parameters Analyzed
1. Viscosity Measurements:
   - Plastic viscosity
   - Apparent viscosity
   - Dynamic viscosity
   - Kinematic viscosity

2. Rheological Properties:
   - Yield point
   - Shear stress/rate relationships
   - Viscoelastic modulus:
     - Elastic modulus
     - Viscous modulus

## Methodology
### Laboratory Analysis
- Haake RS Rheometer 6000 measurements
- High-temperature conditioning (up to 900°F) using electric muffle furnace
- Rheological parameter measurements under various conditions

### Machine Learning Approach
The study employs an ensemble learning method combining:
- Decision Tree Regression
- Linear Regression
- K-Nearest Neighbors (KNN)

### Feature Engineering
- Temperature-density interactions
- Shear stress-rate relationships
- Viscosity parameter correlations

## Directory Structure
```
├── data/              # Data files
├── models/            # Trained model files
├── notebooks/         # Jupyter notebooks
├── src/              # Source code
└── results/          # Analysis results and figures
```

## Installation
```bash
# Clone the repository
git clone https://github.com/ol-s-cloud/heavy-oil-rheology-ml.git

# Install requirements
pip install -r requirements.txt
```

## Future Work
1. Advanced Modeling Approaches:
   - Implementation of Gradient Boosting Regressors
   - Deep Learning models for complex rheological behavior
   - Time series analysis for temperature-dependent properties

2. Enhanced Analysis:
   - Error distribution analysis
   - Uncertainty quantification
   - Cross-validation with different biosolvent combinations
   - Non-linear feature interactions

3. Additional Features:
   - Integration with fluid dynamics simulations
   - Real-time prediction capabilities
   - Web-based visualization interface

## License
This project is licensed under the MIT License - see the LICENSE file for details.