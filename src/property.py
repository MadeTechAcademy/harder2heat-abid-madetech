from src.connectivity import Connectivity


class Property:
    def __init__(self, uprn, connectivity=None, coordinates=None, osid=None, size=None, age_updated_date=None):
        self.uprn = uprn
        self.connectivity = Connectivity.modify(connectivity)
        self.coordinates = coordinates
        self.osid = osid
        self.size = size
        self.age_updated_date = age_updated_date
