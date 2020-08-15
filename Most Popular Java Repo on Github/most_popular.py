import requests
from plotly.graph_objects import Bar
from plotly import offline

url = 'https://api.github.com/search/repositories?q=language:java&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}

r = requests.get(url, headers=headers)
print(f"Status: {r.status_code}")

item_data = r.json()

print(f"Total Count: {item_data['total_count']}")
print(f"Items: {len(item_data['items'])}")

repository_link, stars, labels = [], [], []

items = item_data['items']
for item in items:
    repo_link = item['html_url']
    repo_name = item['name']
    display = f"<a href='{repo_link}'>{repo_name}</a>"

    repository_link.append(display)
    stars.append(item['stargazers_count'])

    owner = item['owner']['login']
    description = item['description']
    text = f"{owner}<br />{description}"
    labels.append(text)


data = [{
    'type': 'bar',
    'x': repository_link,
    'y': stars,
    'hovertext': labels,
    'marker':{
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6
}]

layout = {
    'title': {
        'text': 'Most Starred Java Repositories in Github',
        'x': 0.5
    },
    'xaxis':{
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis':{
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    }
}

fig = {'data': data, 'layout': layout}
offline.plot(fig, filename='java_git_repo.html')