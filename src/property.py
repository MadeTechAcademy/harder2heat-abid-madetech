MINIMUM_EPC_RATING = "C"
MINIMUM_FAILING_AGE = 1959
COLD_CONNECTIVITY = "Standalone"
WARM_MATERIALS = ["Brick Or Block Or Stone", "Contrete"]


class Property:
    def __init__(self, uprn):
        self.uprn = uprn
        self.connectivity = None
        self.coordinates = None
        self.osid = None
        self.property_size = None
        self.age_updated_date = None

    @staticmethod
    def modify_connectivity_description(connectivity_description):
        correct_descriptions = {
            'Standalone': 'Free-Standing',
            'Semi-Connected': 'Single Connected',
            'End-Connected': 'Dual-Connected'
        }

        return correct_descriptions.get(connectivity_description)

    # def calculate_score(self):
    #     score = 0
    #     self.handle_age_string()
    #     if self.connectivity == COLD_CONNECTIVITY:
    #         score += 1
    #     if self.material not in WARM_MATERIALS and self.material != "":
    #         score += 1
    #     if self.epc_rating > MINIMUM_EPC_RATING or self.epc_rating == "":
    #         score += 1
    #     if self.age <= MINIMUM_FAILING_AGE and self.age > 0:
    #         score += 1

    #     self.score = score
    #     return score

    # def handle_age_string(self):
    #     if self.age == "Unknown":
    #         self.age = MINIMUM_FAILING_AGE
    #     age_is_int = type(self.age) is int
    #     if not age_is_int:
    #         self.age = int(self.age[-4:])
