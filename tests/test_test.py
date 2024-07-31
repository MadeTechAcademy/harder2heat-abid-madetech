import json
from src.utils import get_properties_from_os

properties = None
list_of_buildings = None
with open('properties.json') as json_properties:
    list_of_buildings = json.load(json_properties)
    properties = get_properties_from_os(list_of_buildings)


def test_length_of_properties():
    assert len(properties) == 4


def test_get_properties_from_os():
    expected_properties = [
        {"uprn": 100090062842, "connectivity": "Semi-Connected", "material": "Brick Or Block Or Stone", "long": 0.0452889, "lat": 52.4569136},
        {"uprn": 10034160625, "connectivity": "End-Connected", "material": "Brick Or Block Or Stone", "long": 0.0480525, "lat": 52.4577911},
        {"uprn": 100090062297, "connectivity": "Standalone", "material": "Brick Or Block Or Stone", "long": 0.0471489, "lat": 52.4569721},
        {"uprn": 100090060430, "connectivity": "End-Connected", "material": "Brick Or Block Or Stone", "long": 0.0481987, "lat": 52.4579841},
    ]

    properties = get_properties_from_os(list_of_buildings)

    assert len(properties) == len(expected_properties)

    for prop, expected in zip(properties, expected_properties):
        assert prop.uprn == expected["uprn"]
        assert prop.connectivity == expected["connectivity"]
        assert prop.material == expected["material"]
        assert prop.long == expected["long"]
        assert prop.lat == expected["lat"]
