from src.property import Property


def get_properties_from_os(list_of_buildings):
    properties = []
    for building_data in list_of_buildings:
        properties.extend(extract_properties(building_data))
    return properties


def extract_properties(building_data):
    building_properties = building_data.get("properties", {})
    uprn_references = building_properties.get("uprnreference", [])
    coordinates = building_data.get("geometry", {}).get("coordinates", [])
    age_updated_date = building_properties.get("buildingage_updatedate", "")
    size = building_properties.get("geometry_area_m2", 0.0)
    connectivity_description = building_properties.get("connectivity", "")
    osid = building_properties.get("osid", "")

    properties = [
        Property(
            uprn=uprn.get("uprn"),
            connectivity=connectivity_description,
            coordinates=coordinates,
            osid=osid,
            age_updated_date=age_updated_date,
            size=size
        )
        for uprn in uprn_references
    ]

    return properties
