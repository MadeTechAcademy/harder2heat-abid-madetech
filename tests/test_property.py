from src.property import Property


def test_property_properties():
    prop = Property(000, "Semi-Connected", [
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
     ], "osid", 100, "2024-03-13")
    assert prop.uprn == 000
    assert prop.connectivity == "Single Connected"
    assert prop.coordinates == [
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
     ]
    assert prop.osid == "osid"
    assert prop.size == 100
    assert prop.age_updated_date == "2024-03-13"

def test_property_with_missing_data():
    prop = Property(uprn=None)
    assert prop.uprn is None
    assert prop.connectivity is None
    assert prop.coordinates is None
    assert prop.osid is None
    assert prop.size is None
    assert prop.age_updated_date is None