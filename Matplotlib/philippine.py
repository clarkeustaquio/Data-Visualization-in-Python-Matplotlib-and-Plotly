import csv
import datetime
import matplotlib.pyplot as plt

filename = 'data/Philippines_Weather_Temperature.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)

    tmin = header.index('TMIN')
    tmax = header.index('TMAX')
    date = header.index('DATE')
    name_index = header.index('NAME')

    dates, tmin_data, tmax_data = [], [], []
    place_name = ''
    for row in reader:
        current_date = datetime.datetime.strptime(row[date], '%Y-%m-%d')

        try:
            min_data = int(row[tmin])
            max_data = int(row[tmax])

        except ValueError:
            print(f"Missing data for {current_date}")
        
        else:
            if 'BAGUIO' in row[name_index]:
                place_name = row[name_index]

                dates.append(current_date)
                tmin_data.append(min_data)
                tmax_data.append(max_data)


plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, tmin_data, c='blue', alpha=0.5)
ax.plot(dates, tmax_data, c='red', alpha=0.5)

plt.fill_between(dates, tmin_data, tmax_data, facecolor='blue', alpha=0.1)
plt.ylim(40, 90)

title = 'Daily Low and High Temperature | 2019-2020'
title += '\n' + place_name

plt.ylabel('Temperature (F)', fontsize=16)
plt.xlabel('', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.title(title, fontsize=20)
fig.autofmt_xdate()

plt.show()