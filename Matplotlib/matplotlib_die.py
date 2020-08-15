import matplotlib.pyplot as plt

from die import Die

die = Die()

results = [die.roll() for roll_count in range(1000)]
frequencies = [results.count(value) for value in range(1, die.die_side+1)]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.bar(range(1, die.die_side+1), frequencies)

ax.set_title('Rolling Die', fontsize=24)
ax.set_xlabel('Results', fontsize=14)
ax.set_ylabel('Frequency of Result', fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=14)

print(frequencies)
fig.savefig('roll_die_matplotlib.png')
plt.show()
