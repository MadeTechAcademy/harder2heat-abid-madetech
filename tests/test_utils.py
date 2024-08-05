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
        {"uprn": 100090062842, "connectivity": "Semi-Connected", "material": "Brick Or Block Or Stone"},
        {"uprn": 10034160625, "connectivity": "End-Connected", "material": "Brick Or Block Or Stone"},
        {"uprn": 100090062297, "connectivity": "Standalone", "material": "Brick Or Block Or Stone"},
        {"uprn": 100090060430, "connectivity": "End-Connected", "material": "Brick Or Block Or Stone"},
    ]

    assert len(properties) == len(expected_properties)

    for prop, expected in zip(properties, expected_properties):
        assert prop.uprn == expected["uprn"]
        assert prop.connectivity == expected["connectivity"]
        assert prop.material == expected["material"]
