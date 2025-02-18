# Heavy Oil Rheology Machine Learning

## Research Overview

This research presents an innovative machine learning approach to analyze flow properties of heavy crude oil under thermal conditions, focusing on the Agbabu bitumen deposit in Ondo State, Nigeria.

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

## Machine Learning Pipeline Architecture

[Machine Learning Pipeline Architecture](ml_pipeline_architecture.html)

## Project Visualizations

### Shear Stress vs Shear Rate
![Shear Stress vs Shear Rate Graph](research_paper/shear_stress_graph.png)

### Actual vs Predicted Values
![Actual vs Predicted Plot](research_paper/actual_vs_predicted_plot.png)

### SHAP Value Analysis
![SHAP Value Analysis](research_paper/shap_value_analysis.png)

## Research Methodology

The study employs a three-stage SKLearn pipeline with Gradient Boosting and SHAP analysis to investigate thermal-induced changes in bitumen rheological properties.

## Performance Metrics

### Yield Point Prediction
- R² Score: 0.9627
- RMSE: 30.5390 Pa
- MAE: 27.7179 Pa

### Apparent Viscosity Prediction
- R² Score: 0.8428
- RMSE: 2.1546 Pa·s
- MAE: 1.6650 Pa·s

## Key Findings

1. Thermal treatment at 977°F significantly reduced bitumen viscosity
2. Identified critical temperature ranges affecting oil flow properties
3. Demonstrated advanced machine learning approach for non-Newtonian fluid analysis

## Further Reading

### Recommended Publications
1. Martinez-Palou, R., et al. (2011). "Transportation of heavy and extra-heavy crude oil by pipeline: a review." Journal of Petroleum Science and Engineering, 75(3-4), 274-282.

2. Henaut, I., et al. (2003). "Thermal flow properties of heavy oils." Offshore Technology Conference.

3. Saniere, A., et al. (2004). "Pipeline transportation of heavy oils, a strategic, economic and technological challenge." Oil Gas Science and Technology, 59(6), 455-466.

### Related Research Areas
- Non-Newtonian fluid dynamics
- Machine learning in petroleum engineering
- Thermal recovery techniques for heavy oils
- Advanced rheological modeling

## Development Roadmap

(Development Roadmap content remains the same as in previous version)

## Publication Details

- **Title**: Three-Stage Machine Learning Pipeline Ensemble with Gradient Boosting and SHAP Analysis
- **Authors**: Falade, A.A., Sa'id, O., Akinsete, O.O
- **Journal**: Global Journal of Engineering and Technology (GJET)
- **Volume**: 4, Issue 1
- **Date**: January 2025

## Collaboration

Interested in contributing? We welcome researchers, students, and professionals from all disciplines. Create an issue in this repository to start a conversation.

## License

MIT License. See the LICENSE file for complete details.

## Citation

Falade, A.A., et al. (2025). Three-Stage Machine Learning Pipeline Ensemble with Gradient Boosting and SHAP Analysis. Global Journal of Engineering and Technology, 4(1), 16-25.