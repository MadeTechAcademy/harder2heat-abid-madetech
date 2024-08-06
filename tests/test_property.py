from src.property import Property


def test_property_properties():
    prop = Property(000)
    assert prop.uprn == 000
    assert prop.connectivity is None
    assert prop.coordinates is None
    assert prop.osid is None
    assert prop.property_size is None
    assert prop.age_updated_date is None
