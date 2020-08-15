import requests
from plotly.graph_objects import Bar
from plotly import offline
from operator import itemgetter

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status: {r.status_code}")

user_ids = r.json()

comments, label_links = [], []
submissions = []

for user in user_ids[:10]:
    url = f'https://hacker-news.firebaseio.com/v0/item/{user}.json'
    r = requests.get(url)

    data_response = r.json()

    forum_link = f"https://news.ycombinator.com/item?id={user}"
    title = data_response['title']
    label = f"<a href='{forum_link}'>{title}</a>"
    comment = data_response['descendants']
    
    comments.append(comment)
    label_links.append(label)

    submission = {
        'title': label,
        'comment': comment,
    }
    submissions.append(submission)

submissions = sorted(submissions, key=itemgetter('comment'), reverse=True)

data = [{
    'type': 'bar',
    'x': [submission['title'] for submission in submissions],
    'y': [submission['comment'] for submission in submissions],
    # 'x': label_links,
    # 'y': comments,
    'marker':{
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6
}]

layout = {
    'title':{
        'text': 'Hacker News',
        'x': 0.5
    },
    'xaxis':{
        'title': 'Topics',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14}
    },
    'yaxis':{
        'title': 'Most Commented Topics',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14}
    }
}
fig = {'data': data, 'layout': layout}
offline.plot(fig, filename='hacker_news.html')
