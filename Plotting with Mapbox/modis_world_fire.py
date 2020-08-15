import csv
from plotly.graph_objects import Layout, Scattermapbox
from plotly import offline

filename = 'data/MODIS_C6_Global_24h.csv'
# filename = 'data/J1_VIIRS_C2_Global_24h.csv'
mapbox_access_token = 'pk.eyJ1IjoiY2xhcmtldXN0YXF1aW8iLCJhIjoiY2thaDBqbTg4MDJ0czJxcXR2MmpuYXp3ZCJ9.t2hPWtzS60pl2aV7KFPCjQ'

with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)

    lons, lats, brights = [], [], []

    lon_index = header.index('longitude')
    lat_index = header.index('latitude')
    bright_index = header.index('brightness')

    for row in reader:
        lons.append(row[lon_index])
        lats.append(row[lat_index])
        brights.append(row[bright_index])

data = [{
    'type': 'scattermapbox',
    'lon': lons,
    'lat': lats,
    'text': ["Brightness: {}".format(bright) for bright in brights],
    'marker':{
        'size': 5,
        'color': 'firebrick',
    }
}]

fire_layout = Layout(
    title={
        'text':'Daily World Fire - MODIS',
        'x': 0.5
    },
    mapbox={
        'style': 'satellite-streets',
        'accesstoken': mapbox_access_token
    }
)

fig = {'data': data, 'layout': fire_layout}
offline.plot(fig, filename='modis_world_fire.html')
