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
        {"uprn": 100090062842, "connectivity": "Semi-Connected", "osid": "02ae4ae4-6119-4d72-aef9-e56013d25e0d"},
        {"uprn": 10034160625, "connectivity": "End-Connected", "osid": "04f8e016-647e-40e6-bb06-bff6fbea3468"},
        {"uprn": 100090062297, "connectivity": "Standalone", "osid": "0b1107e5-00f8-4d89-b6ae-67f0f98a6517"},
        {"uprn": 100090060430, "connectivity": "End-Connected", "osid": "1384ef24-2e6e-49a2-906f-af35fc12713e"},
    ]

    assert len(properties) == len(expected_properties)

    for prop, expected in zip(properties, expected_properties):
        assert prop.uprn == expected["uprn"]
        assert prop.connectivity == expected["connectivity"]
        assert prop.osid == expected["osid"]
