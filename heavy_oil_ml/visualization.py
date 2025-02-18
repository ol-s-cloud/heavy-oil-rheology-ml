import matplotlib.pyplot as plt
import shap

def plot_actual_vs_predicted(y_test, y_pred, target_name):
    """
    Create an actual vs predicted values plot.

    Args:
        y_test (array-like): True target values
        y_pred (array-like): Predicted target values
        target_name (str): Name of the target variable
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, y_pred, alpha=0.5)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
    plt.xlabel('Actual Values')
    plt.ylabel('Predicted Values')
    plt.title(f'Actual vs Predicted Values - {target_name}')
    plt.tight_layout()
    plt.show()

def plot_shap_values(shap_values, feature_names, target_name):
    """
    Create SHAP summary plot.

    Args:
        shap_values (array-like): SHAP values
        feature_names (list): Names of features
        target_name (str): Name of the target variable
    """
    plt.figure(figsize=(12, 8))
    shap.summary_plot(shap_values, feature_names=feature_names)
    plt.title(f'SHAP Feature Importance - {target_name}')
    plt.tight_layout()
    plt.show()