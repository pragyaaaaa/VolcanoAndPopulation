import itertools

import folium
import pandas as pd


def listOfTuples(latitude, longitude):
    return list(map(lambda x, y: (x, y), latitude, longitude))


data_volcanoes = pd.read_csv("Volcanoes.txt")
data_pop = pd.read_csv("country-coordinates-world.csv")
pop_lat = list(data_pop["latitude"])
pop_long = list(data_pop["longitude"])
pop_country_name = list(data_pop["Country"])
vol_lat = list(data_volcanoes["LAT"])
vol_elev = list(data_volcanoes["ELEV"])
vol_name = list(data_volcanoes["NAME"])
vol_lon = list(data_volcanoes["LON"])
vol_coordinates = listOfTuples(vol_lat, vol_lon)
pop_coordinates = listOfTuples(pop_lat, pop_long)
print(vol_coordinates)
map_f = folium.Map(location=[54.5260, -105.2551], zoom_start=3, tiles="Stamen Terrain")
feature_group = folium.FeatureGroup(name="Volcano and Population")
feature_group_vol = folium.FeatureGroup(name="Volcano and Population")
# for cor in vol_coordinates:
#     print(cor)
for coordinates, place in itertools.zip_longest(pop_coordinates, pop_country_name):
    feature_group.add_child(folium.Marker(location=coordinates, popup=place, icon=folium.Icon(color="red")))

for volcanoes, name, elev in itertools.zip_longest(vol_coordinates, vol_name, vol_elev):
    feature_group_vol.add_child(folium.Marker(location=volcanoes, popup=[name, elev], icon=folium.Icon(color="green")))
map_f.add_child(feature_group)
map_f.add_child(feature_group_vol)
map_f.save("volcanoandmap.html")
