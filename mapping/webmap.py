#!/usr/bin/python3

# Library imports: Folium for mapping/visualization and pandas for data organization
import folium
import pandas

# Create Data Frame object with pandas library storing data from "volcanoes.txt"
data = pandas.read_csv("Volcanoes.txt")

# Separate values from "volcanoes.txt" into separate lists to iterate through later
lat_list = list(data["LAT"])
lon_list = list(data["LON"])
elev_list = list(data["ELEV"])
type_list = list(data["TYPE"])
status_list = list(data["STATUS"])
name_list = list(data["NAME"])

# Create html variable to format what the iframe popup on the map should look like
html = """<h4>Volcano Information:</h4>
<strong>Name</strong>: <a href="http://www.google.com/search?q=%s" target="_blank">%s</a><br>
<strong>Height</strong>: %s m <br>
<strong>Type</strong>: %s <br>
<strong>Status</strong>: %s <br>
"""

# function to choose a marker color based on volcano elevation
def marker_color(elevation):
    if elevation < 1000:
        return "green"
    elif elevation >= 1000 and elevation < 3000:
        return "orange"
    else:
        return "red"

# Create Map object as first layer 
map = folium.Map(location=[38.600869, -121.495411], zoom_start=5, tiles="Stamen Terrain")

# Create Folium feature groups for both volcanoes and population to separate into different layers
mg = folium.FeatureGroup(name="Volcanoes")
cg = folium.FeatureGroup(name="Population")

# Loop through the lat and lon lists above using individual lat/lon pairs to create markers on the map.
for lat, lon, name, el, typ, stat in zip(lat_list, lon_list, name_list, elev_list, type_list, status_list):
    # Create iframe object to use the html variable from earlier and fill in various pieces of info
    iframe = folium.IFrame(html=html % (name, name, str(el), typ, stat), width=250, height=150)

    # Color code markers based on elevation value using marker_color function
    mg.add_child(folium.CircleMarker(location=[lat, lon], popup=folium.Popup(iframe), radius=8, fill_opacity=0.9, color="gray",
    fill_color=marker_color(el)))

# Create geometrical shapes around countries that can be filled in with different colors depending on their population
cg.add_child(folium.GeoJson(data=open("world.json", 'r', encoding='utf-8-sig').read(), 
    style_function=lambda x: {'fillColor':'green' if x["properties"]['POP2005'] < 10000000
    else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

# Add feature group information(volcanoes and population layers) to the map object
map.add_child(mg)
map.add_child(cg)

# Add layer control menu for functionality in turning off specific layers
map.add_child(folium.LayerControl())

# Save the map to an HTML file
map.save("Map1.html")

