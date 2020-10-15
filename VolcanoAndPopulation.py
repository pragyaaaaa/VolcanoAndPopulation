import folium

map_f = folium.Map(location=[54.5260, -105.2551], zoom_start=3, tiles="Stamen Terrain")
map_f.save("volcanoandmap.html")
