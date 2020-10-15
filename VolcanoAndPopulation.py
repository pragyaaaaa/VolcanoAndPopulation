import folium

map_f = folium.Map(location=[54.5260, -105.2551], zoom_start=3, tiles="Stamen Terrain")
feature_group = folium.FeatureGroup(name="Volcano and Population")
feature_group.add_child(folium.Marker(location=[37.0902, -95.7129], popup="USA", icon=folium.Icon(color="red")))
map_f.add_child(feature_group)
map_f.save("volcanoandmap.html")
