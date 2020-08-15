import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_2018_simple.csv'
death_valley = 'data/death_valley_2018_simple.csv'
try:
    with open(filename) as f:
        reader = csv.reader(f)
        header = next(reader)

        daily_prcp, dates = [], []
        for row in reader:
            date = datetime.strptime(row[2], '%Y-%m-%d')
            try:
                daily_prcp_amount = float(row[3])
            except ValueError:
                print(f"Missing data for {date}")
            else:
                dates.append(date)
                daily_prcp.append(daily_prcp_amount)

except FileNotFoundError:
    pass
else:
    plt.style.use('seaborn')
    
    fig, ax = plt.subplots()
    ax.plot(dates, daily_prcp, c='red')

    plt.title('Sitka Daily Precipitation', fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel('Rainfall (in)', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

