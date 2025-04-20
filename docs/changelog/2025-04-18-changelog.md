# Changelog

All notable changes to the Heavy Oil Rheology ML project (RheoML) will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2025-04-18

### Added
- Initial release of the Heavy Oil Rheology ML project
- Three-stage machine learning pipeline implementation:
  - Data preparation and feature engineering
  - Machine learning with Gradient Boosting
  - Evaluation and SHAP analysis
- Core functionality for analyzing rheological properties of heavy crude oil
- Support for Haake RS 6000 Rheometer data
- Basic visualization utilities for model outputs
- Documentation including README, CONTRIBUTING, and CODE_OF_CONDUCT

### Data Processing
- Implemented data normalization for temperature and shear rate
- Added feature engineering for derived rheological properties
- Created data pipeline for preprocessing experimental measurements

### Machine Learning
- Implemented Gradient Boosting Regressor with the following hyperparameters:
  - n_estimators=100
  - learning_rate=0.1
  - max_depth=3
  - random_state=42
- Added model evaluation metrics (RMSE, R², MAE)
- Implemented SHAP analysis for model explainability

### Documentation
- Added comprehensive project documentation structure
- Created historical tracking for:
  - Gap analysis
  - Project status
  - Project vision
  - Sprint planning
  - Technical specifications
- Added device compatibility guide for rheometer devices
- Created product roadmap for future development

## [Unreleased]

### Planned
- Web interface for data entry and visualization
- Enhanced data ingestion for multiple rheometer devices
- Expanded machine learning model options
- Interactive dashboards for result analysis
- API for external system integration

See the [roadmap](../roadmap/2025-04-18-product-roadmap.md) for detailed information about planned features and timelines.

---

## Previous Development History (Pre-Release)

### [Research Prototype] - 2024-11-15
- Initial implementation of Gradient Boosting for rheological prediction
- Basic SHAP integration for feature importance analysis
- Exploratory data analysis of heavy oil samples
- Testing with limited experimental dataset

### [Experimental Setup] - 2024-09-20
- Data collection protocol established
- Initial testing with Haake RS 6000 Rheometer
- Basic data structures defined
- Configuration of experimental parameters

### [Research Conception] - 2024-07-10
- Project idea formulated
- Literature review on heavy oil rheology
- Survey of machine learning approaches for rheological analysis
- Identification of key research questions