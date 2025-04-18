# Device Compatibility Guide

*Date: April 18, 2025*

This document provides comprehensive information about rheometer device compatibility with the RheoML platform. It serves as a reference for researchers and industry professionals who wish to use RheoML with their existing equipment or who are evaluating new equipment purchases.

## Reference Device

The RheoML platform was initially developed using the **Haake RS 6000 Rheometer** from Thermo Scientific. This device serves as our reference implementation with the following specifications:

**Haake RS 6000 Rheometer**:
- **Manufacturer**: Thermo Scientific
- **Key Features**:
  - Four-bladed vane-type rotor (FL40)
  - Diameter: 40 mm
  - Gap width: 1.5 mm
  - Coaxial cylinder sensor system (Z38 DIN)
  - Sample capacity: 30.8 cm³
  - Liquid temperature-controlled system

## Compatibility Matrix

The following table provides a comprehensive comparison of various rheology devices based on their compatibility with RheoML:

| **Manufacturer** | **Device** | **Equivalent to HAAKE RS 6000** | **Green Solvent Compatibility** | **Material Limitations** | **ML Model Applicability** |
|-----------------|------------|----------------------------------|--------------------------------|--------------------------|----------------------------|
| **Thermo Scientific** | HAAKE MARS Series | ✅ Yes | ✅ Likely compatible | Some high-viscosity limits | High compatibility; ML models trained on HAAKE RS 6000 data can be adapted with minimal adjustments. |
| | HAAKE Viscotester iQ | ❌ No (simpler tool) | ❌ Limited | Low-viscosity samples only | Limited; significant modifications to ML models required due to device constraints. |
| **TA Instruments** | ARES-G2 Rheometer | ✅ Yes | ✅ Likely compatible | Some temperature constraints | High compatibility; ML models can be adapted with consideration of temperature constraints. |
| | DHR Series | ✅ Yes | ✅ Likely compatible | May need solvent-resistant accessories | High compatibility; ensure solvent-resistant accessories are used when necessary. |
| **Anton Paar** | MCR Rheometer Series | ✅ Yes | ✅ Compatible with accessories | High precision but limited to lab-scale | High compatibility; ML models can be applied effectively, considering lab-scale limitations. |
| **Malvern Panalytical** | Kinexus Rheometers | ✅ Yes | ✅ Likely compatible | Depends on solvent compatibility kits | High compatibility; verify solvent compatibility kits are in place. |
| **Brookfield** | DVNext Rheometer | ❌ No (simpler tool) | ❌ Limited | Low-stress testing only | Limited; ML models require significant adjustments due to device simplicity. |
| **KRUSS Scientific** | KRUSS Rheometers | ✅ Possibly | ✅ Designed for scientific research | May have sample size constraints | Moderate compatibility; ML models may need calibration for sample size variations. |
| **Qualitest** | Polymer Rheometers | ✅ Yes (For polymers) | ❌ Limited | Focuses on thermoplastics/elastomers | Limited; ML models specific to polymers may be applicable, but not for other materials. |

## ML Model Generalization Across Devices

### Key Considerations for Cross-Device ML Application

1. **Data Consistency**
   - ML models trained on data from the HAAKE RS 6000 require recalibration when applied to data from other devices
   - Different measurement techniques and sensitivities across manufacturers necessitate calibration factors
   - Data normalization is critical for consistent predictions across devices

2. **Solvent Compatibility**
   - When introducing green solvents, device material compatibility must be verified
   - RheoML's ML models incorporate solvent properties as variables to maintain prediction accuracy
   - Solvent viscosity and interaction effects are considered in model training

3. **Material Limitations**
   - Some devices are optimized for specific materials (e.g., polymers)
   - Applying ML models across different materials requires consideration of rheological properties unique to each substance
   - Material-specific calibration may be necessary for optimal results

4. **Measurement Range Considerations**
   - Devices differ in their measurement ranges for:
     - Shear rate
     - Viscosity
     - Temperature
     - Torque
   - ML models must account for these differences through appropriate scaling and normalization

## Integration Guidance

### Data Format Requirements

For optimal compatibility with RheoML, data from different rheometers should include:

1. **Required Parameters**:
   - Shear rate (1/s)
   - Shear stress (Pa)
   - Temperature (°C)
   - Sample density (g/cm³) if available

2. **Recommended Additional Parameters**:
   - Viscosity (Pa·s)
   - Normal force (N)
   - Oscillatory measurements (if available)
   - Sample preparation details

### Device-Specific Integration Notes

#### Thermo Scientific Devices

- **HAAKE MARS Series**: Direct compatibility with minimal adjustments
- **HAAKE Viscotester iQ**: Limited to lower viscosity samples; requires adjustment factors for predictions

#### TA Instruments

- **ARES-G2**: Consider temperature limitations when applying models
- **DHR Series**: Ensure appropriate accessories for solvent compatibility

#### Anton Paar

- **MCR Series**: High precision data may require downsampling for model compatibility
- Scale considerations for lab-scale to industrial applications

#### Malvern Panalytical

- **Kinexus**: Verify solvent compatibility kit installation for green solvent usage
- Calibration against reference standards recommended

## Future Compatibility Roadmap

RheoML's device compatibility will expand according to the following roadmap:

1. **Phase 1** (Q2-Q3 2025):
   - Complete integration with Thermo Scientific HAAKE Series
   - Basic support for TA Instruments ARES-G2 and DHR Series

2. **Phase 2** (Q4 2025-Q1 2026):
   - Full support for Anton Paar MCR Series
   - Integration with Malvern Panalytical Kinexus

3. **Phase 3** (Q2-Q4 2026):
   - Support for specialty devices (KRUSS, Qualitest)
   - Integration with IoT-enabled rheometers and real-time data streams

## Conclusion

While RheoML's ML models offer powerful predictive capabilities, their successful application across various rheological instruments and conditions depends on careful calibration and validation. Ensuring that device specifications align with experimental conditions is crucial for accurate and reliable predictions.

For specific integration questions or to request support for additional devices, please contact the RheoML development team or open an issue on the GitHub repository.