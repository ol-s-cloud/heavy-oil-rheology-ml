class ModelRegistry:
    def __init__(self, tier='community'):
        """
        Manage ML model registrations and versions

        Args:
            tier (str): Access tier for model capabilities
        """
        self.tier = tier
        self.models = {}

    def register(self, name, model, version='0.1.0'):
        """
        Register a new ML model

        Args:
            name (str): Model name
            model (object): Model instance
            version (str): Model version
        """
        self.models[name] = {
            'model': model,
            'version': version
        }

    def get(self, name):
        """
        Retrieve a registered model

        Args:
            name (str): Model name
        """
        return self.models.get(name)