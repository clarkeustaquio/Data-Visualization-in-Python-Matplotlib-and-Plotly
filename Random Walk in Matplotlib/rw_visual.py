import matplotlib.pyplot as plt

from random_walk import RandomWalk
while True:
    random_walk = RandomWalk(50_000)
    random_walk.fill_walk()

    plt.style.use('classic')

    fix, ax = plt.subplots(figsize=(15, 9))
    point_number = range(random_walk.num_points)

    # ax.plot(random_walk.x_values, random_walk.y_values, linewidth=3)
    
    ax.scatter(random_walk.x_values, random_walk.y_values,
        c=point_number, cmap=plt.cm.Blues, edgecolors='none', s=1)

    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(random_walk.x_values[-1], random_walk.y_values[-1],
        c='red', edgecolors='none', s=100)


    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    keep_running = input('Make another walk? (ny/n): ')
    if keep_running == 'n':
        break

#page 361 rolling dice