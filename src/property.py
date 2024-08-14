class Property:
    def __init__(self, uprn, connectivity=None, coordinates=None, osid=None, size=None, age_updated_date=None):
        self.uprn = uprn
        self.connectivity = self.modify_connectivity_description(connectivity)
        self.coordinates = coordinates
        self.osid = osid
        self.size = size
        self.age_updated_date = age_updated_date

    @staticmethod
    def modify_connectivity_description(connectivity_description):
        correct_descriptions = {
            'Standalone': 'Free-Standing',
            'Semi-Connected': 'Single Connected',
            'End-Connected': 'Dual-Connected'
        }

        return correct_descriptions.get(connectivity_description, connectivity_description)
