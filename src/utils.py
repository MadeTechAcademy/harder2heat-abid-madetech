from src.property import Property


# def get_properties_from_os(list_of_buildings):
#     list_of_properties = []
#     for i in range(len(list_of_buildings)):
#         building = list_of_buildings[i]["properties"]
#         uprn_array = building["uprnreference"]
#         for j in range(len(uprn_array)):
#             new_prop = Property(uprn_array[j]["uprn"])
#             new_prop.connectivity = new_prop.modify_connectivity_description(building["connectivity"])
#             new_prop.osid = building["osid"]
#             new_prop.coordinates = list_of_buildings[i]["geometry"]["coordinates"]
#             new_prop.age_updated_date = building["buildingage_updatedate"]
#             new_prop.size = building["geometry_area_m2"]
#
#             list_of_properties.append(new_prop)
#
#     return list_of_properties

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
