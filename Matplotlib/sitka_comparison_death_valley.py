import csv
import matplotlib.pyplot as plt
from datetime import datetime

def get_weather(filename, dates, lows,
    highs, date_index, low_index, high_index):

    with open(filename) as f:
        reader = csv.reader(f)
        header = next(reader)

        for row in reader:
            date = datetime.strptime(row[date_index], '%Y-%m-%d')
            try:
                low = int(row[low_index])
                high = int(row[high_index])
            except ValueError:
                print(f"Missing data for {date}")
            else:
                dates.append(date)
                lows.append(low)
                highs.append(high)

plt.style.use('seaborn')
fig, ax = plt.subplots()

sitka = 'data/sitka_weather_2018_simple.csv'
dates, lows, highs = [], [], []
get_weather(sitka, dates, lows, highs, date_index=2, 
            low_index=5, high_index=6)

ax.plot(dates, lows, c='blue', alpha=0.6)
ax.plot(dates, highs, c='red', alpha=0.6)
plt.fill_between(dates, lows, highs, facecolor='blue', alpha=0.15)


death_valley = 'data/death_valley_2018_simple.csv'
dates, lows, highs = [], [], []
get_weather(death_valley, dates, lows, highs, date_index=2,
            low_index=4, high_index=5)

ax.plot(dates, lows, c='blue', alpha=0.3)
ax.plot(dates, highs, c='red', alpha=0.3)
plt.fill_between(dates, lows, highs, facecolor='blue', alpha=0.15)

title = 'Daily high and low temperature - 2018'
title += '\nSitka, AK and Death Valley, CA'

plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()

plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.ylim(10, 130)


plt.show()