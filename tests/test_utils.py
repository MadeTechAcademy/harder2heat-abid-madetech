import json
from src.utils import get_properties_from_os
from src.property import Property

properties = None
list_of_buildings = None
with open('properties.json') as json_properties:
    list_of_buildings = json.load(json_properties)
    properties = get_properties_from_os(list_of_buildings)

expected_properties = [
    {"uprn": 100090062842, "connectivity": "Semi-Connected", "osid": "02ae4ae4-6119-4d72-aef9-e56013d25e0d",
     "age_updated_date": "2024-05-20",
     "coordinates": [
         [
             [
                 0.0452889,
                 52.4569136
             ],
             [
                 0.0453246,
                 52.4569215
             ],
             [
                 0.045323,
                 52.4569242
             ],
             [
                 0.0453908,
                 52.4569392
             ],
             [
                 0.0454023,
                 52.4569199
             ],
             [
                 0.0455166,
                 52.4569451
             ],
             [
                 0.0455493,
                 52.4568931
             ],
             [
                 0.0453653,
                 52.4568526
             ],
             [
                 0.0453603,
                 52.456861
             ],
             [
                 0.0453246,
                 52.4568531
             ],
             [
                 0.0452889,
                 52.4569136
             ]
         ]
     ]},
    {"uprn": 10034160625, "connectivity": "End-Connected", "osid": "04f8e016-647e-40e6-bb06-bff6fbea3468",
     "age_updated_date": "2024-03-13",
     "coordinates": [
         [
             [
                 0.0480525,
                 52.4577911
             ],
             [
                 0.0481155,
                 52.4578076
             ],
             [
                 0.0481554,
                 52.4577508
             ],
             [
                 0.0480922,
                 52.4577343
             ],
             [
                 0.0480525,
                 52.4577911
             ]
         ]
     ]},
    {"uprn": 100090062297, "connectivity": "Standalone", "osid": "0b1107e5-00f8-4d89-b6ae-67f0f98a6517",
     "age_updated_date": "2024-03-13",
     "coordinates": [
         [
             [
                 0.0471489,
                 52.4569721
             ],
             [
                 0.0472922,
                 52.4569964
             ],
             [
                 0.0473205,
                 52.4569337
             ],
             [
                 0.0473576,
                 52.45694
             ],
             [
                 0.0473707,
                 52.4569112
             ],
             [
                 0.0473336,
                 52.4569049
             ],
             [
                 0.0473464,
                 52.4568765
             ],
             [
                 0.0472657,
                 52.4568629
             ],
             [
                 0.0472642,
                 52.4568662
             ],
             [
                 0.0472467,
                 52.4568633
             ],
             [
                 0.0472399,
                 52.4568621
             ],
             [
                 0.0472175,
                 52.4569117
             ],
             [
                 0.0472229,
                 52.4569126
             ],
             [
                 0.0472151,
                 52.4569296
             ],
             [
                 0.0472085,
                 52.456944
             ],
             [
                 0.047165,
                 52.4569366
             ],
             [
                 0.0471489,
                 52.4569721
             ]
         ]
     ]},
    {"uprn": 100090060430, "connectivity": "End-Connected", "osid": "1384ef24-2e6e-49a2-906f-af35fc12713e",
     "age_updated_date": "2024-03-13",
     "coordinates": [
         [
             [
                 0.0481987,
                 52.4579841
             ],
             [
                 0.0482696,
                 52.458004
             ],
             [
                 0.0483139,
                 52.4579451
             ],
             [
                 0.0482431,
                 52.4579252
             ],
             [
                 0.0481987,
                 52.4579841
             ]
         ]
     ]},
]


def test_length_of_properties():
    assert len(properties) == 4


def test_get_properties_from_os():
    assert len(properties) == len(expected_properties)

    for prop, expected in zip(properties, expected_properties):
        assert isinstance(prop, Property)
        assert prop.uprn == expected["uprn"]
        assert prop.connectivity == expected["connectivity"]
        assert prop.osid == expected["osid"]
        assert prop.coordinates == expected["coordinates"]
        assert prop.age_updated_date == expected["age_updated_date"]
