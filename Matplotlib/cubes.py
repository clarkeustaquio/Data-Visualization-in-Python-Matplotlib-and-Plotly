import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('bmh')
fig, ax = plt.subplots()
# ax.plot(x_values, y_values, linewidth=3)
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.YlGnBu,s=10)
ax.set_title("Cube of a Number", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cubic Value", fontsize=14)

ax.tick_params(axis='both', which='minor', labelsize=14)

# ax.axis([0, 5100, 0, y_values[-1]])
plt.show()