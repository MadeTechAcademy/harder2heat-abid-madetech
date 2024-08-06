from src.property import Property

def get_properties_from_os(list_of_buildings):
    list_of_properties = []
    for i in range(len(list_of_buildings)):
        coordinates = list_of_buildings[i]["geometry"]["coordinates"][0][0]
        building = list_of_buildings[i]["properties"]
        uprn_array = building["uprnreference"]
        for j in range(len(uprn_array)):
            new_prop = Property(uprn_array[j]["uprn"])
            new_prop.connectivity = building["connectivity"]
            new_prop.osid = building["osid"]
            new_prop.coordinates = list_of_buildings[i]["geometry"]["coordinates"]

            list_of_properties.append(new_prop)

    return list_of_properties

            









