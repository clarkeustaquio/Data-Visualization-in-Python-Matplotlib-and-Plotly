from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

die = Die()
die_2 = Die()
# die_3 = Die()

results = [die.roll() + die_2.roll() for roll_num in range(1000)]

# for roll_num in range(1000):
#     result = die.roll() * die_2.roll() #+ die_3.roll()
#     results.append(result)

max_result = die.die_side + die_2.die_side #+ die_3.die_side
frequencies = [results.count(value) for value in range(2, max_result+1)]

# for value in range(1, max_result+1):
#     frequency = results.count(value)
#     frequencies.append(frequency)

x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_configuration = {'title': 'Result', 'dtick': 1}
y_axis_configuration = {'title': 'Frequency of Result'}

my_layout = Layout(title={'text':'Results of rolling a 2-D6 multiplied 1000 times', 'xanchor': "auto", 'yanchor': "auto"},
   xaxis=x_axis_configuration, yaxis=y_axis_configuration)

offline.plot({'data': data, 'layout': my_layout,}, filename='d6_xd6.html')


# print(results)
print(frequencies)