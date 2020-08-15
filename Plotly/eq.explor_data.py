import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/eq_data_30_day_m1.json'

with open(filename) as f:
    all_eq_data = json.load(f)

# readable_file = 'data/readable_eq_data.json'
# with open(readable_file, 'w') as f:
#     json.dump(all_eq_data, f, indent=4)

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

mags, lons, lats, hover_text = [], [], [], []
title = all_eq_data['metadata']['title']
for eq_dicts in all_eq_dicts:
    mags.append(eq_dicts['properties']['mag'])
    lons.append(eq_dicts['geometry']['coordinates'][0])
    lats.append(eq_dicts['geometry']['coordinates'][1])
    hover_text.append(eq_dicts['properties']['title'])


print(mags[:10])
print(lons[:5])
print(lats[:5])

# data = [Scattergeo(lon=lons, lat=lats)]
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_text,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'}
    }
}]
my_layout = Layout(title={'text': title, 'x': 0.5})

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
