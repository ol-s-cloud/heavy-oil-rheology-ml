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
    plot_actual_vs_predicted(
        y_test=result['y_test'], 
        y_pred=result['y_pred'], 
        target_name=target
    )
    
    plot_shap_values(
        shap_values=result['shap_values'], 
        feature_names=result['poly_feature_names'], 
        target_name=target
    )
```

## Development Roadmap v0.1.0 (Current)

### Completed
- [x] Research and initial machine learning pipeline development
- [x] Experimental data collection and preprocessing
- [x] Machine learning model training and evaluation
- [x] Performance metrics and SHAP analysis

### Planned Features
- [ ] Develop portable machine learning model
- [ ] Create data preprocessing scripts
- [ ] Implement SHAP analysis toolkit
- [ ] Develop basic CLI interface
- [ ] Design responsive web application

## Contributions

We welcome contributions from researchers, students, and professionals interested in machine learning, petroleum engineering, and data science. Here are five key ways to contribute:

1. **Research Collaboration**
   - Propose improvements to the machine learning pipeline
   - Share additional rheological datasets
   - Develop new feature engineering techniques

2. **Code Development**
   - Improve existing machine learning models
   - Enhance data preprocessing scripts
   - Develop new visualization tools
   - Implement additional performance metrics

3. **Testing and Validation**
   - Run experiments with different crude oil samples
   - Validate model performance across various conditions
   - Develop comprehensive unit tests
   - Create integration test suites

4. **Documentation**
   - Improve code documentation
   - Create tutorials and usage examples
   - Write detailed API documentation
   - Develop comprehensive README and user guides

5. **Community Engagement**
   - Report issues and suggest improvements
   - Participate in code reviews
   - Help triage and reproduce reported bugs
   - Contribute to discussion of project roadmap

Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for our community standards.

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

The study utilized the Haake RS 6000 Rheometer, a sophisticated instrument for precise rheological measurements.

- **Manufacturer**: Thermo Scientific
- **Model**: Haake RS 6000
- **Key Features**: 
  - Four-bladed vane-type rotor (FL40)
  - Diameter: 40 mm
  - Gap width: 1.5 mm
  - Coaxial cylinder sensor system (Z38 DIN)
  - Sample capacity: 30.8 cm³
  - Liquid temperature-controlled system

#### Device Specifications
- **Brochure**: [Haake RS 6000 Rheometer Brochure](https://tools.thermofisher.com/content/sfs/brochures/D11480~.pdf)

## Publication Details
- **Title**: Three-Stage Machine Learning Pipeline Ensemble with Gradient Boosting and SHAP Analysis
- **Authors**: Falade, A.A., Sa'id, O., Akinsete, O.O
- **Journal**: Global Journal of Engineering and Technology (GJET)
- **Volume**: 4, Issue 1
- **Date**: January 2025

## License
MIT License. See the LICENSE file for complete details.

## Citation
Falade, A.A., Sa'id, O., Akinsete, O.O. (2025). Three-Stage Machine Learning Pipeline Ensemble with Gradient Boosting and SHAP Analysis. Global Journal of Engineering and Technology, 4(1), 16-25.