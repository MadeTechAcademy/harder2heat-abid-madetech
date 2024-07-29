import json
from src.utils import get_properties_from_os


def test_pytest_works():
    assert True == True


def test_length_of_properties():
    properties = None
    with open('properties.json') as json_properties:
        data = json.load(json_properties)
        properties = get_properties_from_os(data)
    assert len(properties) == 4
