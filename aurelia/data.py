import pandas as pd

class DataHandler:
    @staticmethod
    def load(source, tier='community'):
        """
        Load data from various sources

        Args:
            source (str): Data source path
            tier (str): Access tier for data loading
        """
        # Basic data loading with tier-based restrictions
        if tier == 'community':
            # Limit data size or features for community tier
            pass
        
        return pd.read_csv(source)