import json
from plotly.graph_objs import Layout, Scattergeo
from plotly import offline


filename = 'data/eq_all_week.json'
with open(filename) as f:
    all_day = json.load(f)

# filename = 'data/readable_eq_all_day.json'

# with open(filename, 'w') as f:
#     json.dump(all_day, f, indent=4)
eq_all_day = all_day['features']
title = all_day['metadata']['title']
magnitudes, longitudes, latitudes, hover_text = [], [], [], []

for eq_day in eq_all_day:
    magnitudes.append(eq_day['properties']['mag'])
    longitudes.append(eq_day['geometry']['coordinates'][0])
    latitudes.append(eq_day['geometry']['coordinates'][1])
    hover_text.append(eq_day['properties']['title'])

data = [{
    'type': 'scattergeo',
    'lon': longitudes,
    'lat': latitudes,
    'text': hover_text,
    'marker': {
        'size': [mag *-1 if mag < 0 else 5*mag for mag in magnitudes],
        'color': magnitudes,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'}
    }
    
}]

geo_layout = Layout(title={'text': title, 'x': 0.5})
figure = {'data': data, 'layout': geo_layout}
offline.plot(figure, filename='recent_global_earthquake.html')
