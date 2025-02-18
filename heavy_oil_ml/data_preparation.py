import pandas as pd
import numpy as np

def prepare_data():
    """
    Prepare and combine data from three tables: Table 4.1, Table 4.2.1, and Table 4.2.2.
    Adds new features for model training and analysis.

    Returns:
        pd.DataFrame: Combined and preprocessed dataset.
    """
    # Table 4.1: Kinematic and Dynamic Viscosity under Standard and Thermal Conditions
    data_41 = {
        "Density": [0.95, 0.95],
        "Temperature": [60, 977],
        "Dynamic Viscosity": [7.7672, 2.014],
        "Kinematic Viscosity": [8.176, 2.120],
    }

    # Table 4.2.1: Shear Rate Rheology for Natural Bitumen
    data_421 = {
        "Shear Stress": [0, 225, 325, 350, 360, 455, 375, 433.5, 494, 510, 550, 525],
        "Shear Rate": [0, 40, 45, 50, 60, 70, 80, 90, 100, 110, 120, 125],
        "Apparent Viscosity": [0, 5.625, 7.222, 7.0, 6.0, 6.5, 4.6875, 4.8167, 4.94, 4.6364, 4.5833, 4.2],
        "Plastic Viscosity": [3.894] * 12,
        "Yield Point": [0, 69.24, 149.77, 155.3, 126.36, 182.42, 63.48, 83.04, 104.6, 81.66, 82.72, 38.25],
    }

    # Table 4.2.2: Apparent Viscosity for Natural Bitumen at 977°F
    data_422 = {
        "Shear Stress": [0, 225, 325, 350, 360, 455, 375, 433.5, 494, 510, 550, 525],
        "Shear Rate": [0, 3, 9, 15, 22, 32, 40, 47, 55, 61, 67, 72],
        "Apparent Viscosity": [0, 75.0, 36, 32, 16, 14, 9.375, 9.2234, 8.98182, 8.36066, 8.20896, 7.39437],
        "Plastic Viscosity": [0.1433] * 12,
        "Yield Point": [0, 224.57, 323.71, 347.85, 356.85, 450.41, 369.27, 426.76, 486.12, 501.26, 540.40, 514.68],
    }

    # Convert tables into DataFrames
    df_41 = pd.DataFrame(data_41)
    df_421 = pd.DataFrame(data_421)
    df_422 = pd.DataFrame(data_422)

    # Add dataset labels for identification
    df_421["Dataset"] = "Table 4.2.1"
    df_422["Dataset"] = "Table 4.2.2"

    # Combine all data into a single DataFrame
    data_combined = pd.concat([df_421, df_422], ignore_index=True)

    # Add density and temperature columns from Table 4.1
    data_combined["Density"] = 0.95
    data_combined["Temperature"] = np.linspace(60, 977, len(data_combined))

    # Feature engineering: create additional features for better modeling
    data_combined["Shear_Stress_Rate_Ratio"] = data_combined["Shear Stress"] / (data_combined["Shear Rate"] + 1e-6)
    data_combined["Temperature_Density_Product"] = data_combined["Temperature"] * data_combined["Density"]

    return data_combined