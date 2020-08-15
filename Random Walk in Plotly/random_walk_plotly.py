from plotly.graph_objs import Layout, Scatter
from plotly import offline
from random_walk import RandomWalk

random_walk = RandomWalk(50_000)
random_walk.fill_walk()
point_number = random_walk.num_points   

data = [Scatter(
    x=random_walk.x_values, 
    y=random_walk.y_values, 
    mode='markers',
    marker=dict(
        size=1,
        gradient=dict(
            type='none',
            color='yellow'
        ),
        color=list(range(point_number)), #'firebrick'
        colorscale= 'Blues', #'YlGnBu' #not going to work if the color is set as a plain color; not a list
        showscale=True,),

    ),
    Scatter(
        x=[random_walk.x_values[0]],
        y=[random_walk.y_values[0]],
        mode='markers',
        marker=dict(
            size=10,
            color='green'
        ),
        
    ),
    Scatter(
        x=[random_walk.x_values[-1]],
        y=[random_walk.y_values[-1]],
        mode='markers',
        marker=dict(
            size=10,
            color='red'
        )
    )
    ]

walk_layout = Layout(title='Random Walk', template='plotly', showlegend=False,
    xaxis={'visible':False}, yaxis={'visible':False})


offline.plot({'data': data, 'layout': walk_layout}, filename='random_walk.html')