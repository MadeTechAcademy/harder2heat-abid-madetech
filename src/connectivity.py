class Connectivity:
    description_map = {
        'Standalone': 'Free-Standing',
        'Semi-Connected': 'Single Connected',
        'End-Connected': 'Dual-Connected'
    }

    @classmethod
    def modify(cls, connectivity_description):
        return cls.description_map.get(connectivity_description, connectivity_description)
