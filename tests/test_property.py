from src.property import Property

def test_property_properties():
    prop = Property(000)
    assert prop.uprn == 000
    assert prop.connectivity is None
