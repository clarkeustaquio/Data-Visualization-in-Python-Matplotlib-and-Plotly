import csv
from plotly import offline
from plotly.graph_objs import Layout, Scattermapbox, Scattergeo
import plotly.graph_objects as go

filename = 'data/world_fires_1_day.csv'
# mapbox_access_token = open(".mapbox_token").read()
mapbox_access_token = 'pk.eyJ1IjoiY2xhcmtldXN0YXF1aW8iLCJhIjoiY2thaDBqbTg4MDJ0czJxcXR2MmpuYXp3ZCJ9.t2hPWtzS60pl2aV7KFPCjQ'

with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)

    lons, lats, brights = [], [], []

    lat_index = header.index('latitude')
    lon_index = header.index('longitude')
    bright_index = header.index('brightness')

    for data in reader:
        lons.append(data[lon_index])
        lats.append(data[lat_index])
        brights.append(float(data[bright_index]))

data = [{
    'type': 'scattermapbox',
    'lon': lons,
    'lat': lats,
    'text': ['Brightness: {}'.format(bright) for bright in brights],
    'marker':{
        'size': 5,
        'color': 'firebrick',
        # 'colorscale': 'Viridis',
        # 'reversescale': True,
        # 'colorbar': {'title': 'Brightness'}
    }
}]


fire_layout = Layout(
    title= {'text': 'Daily World Fire', 'x': 0.5},
    mapbox= {
        'style': 'satellite-streets',
        'accesstoken': mapbox_access_token
        }
    )
fig = {'data': data, 'layout': fire_layout}

offline.plot(fig, filename='world_fire.html')
