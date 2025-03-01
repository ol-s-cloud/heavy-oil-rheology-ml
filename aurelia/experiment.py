class Experiment:
    def __init__(self, domain=None, tier='community'):
        """
        Create a new scientific experiment

        Args:
            domain (str): Research domain
            tier (str): Access tier (community, research, enterprise)
        """
        self.domain = domain
        self.tier = tier
        self._validate_tier()

    def _validate_tier(self):
        """Validate and set experiment tier"""
        valid_tiers = ['community', 'research', 'enterprise']
        if self.tier not in valid_tiers:
            raise ValueError(f"Invalid tier. Choose from {valid_tiers}")