import csv
from datetime import datetime
from matplotlib import pyplot as plt
# Obtém as temperaturas máximas do arquivo
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date,'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    #print(highs)
    # Faz a plotagem dos dados
    fig = plt.figure(dpi=128, figsize=(10,6))
    plt.plot(dates, highs,c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue',alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='green', alpha=0.2)
    # Formata o gráfico
    title = 'Daily high and low temperatures - 2014\nDeath Valley, CA'
    plt.title(title, fontsize=20)
    plt.xlabel('', fontsize = 16)
    fig.autofmt_xdate()
    plt.ylabel('Temprature (F)',fontsize=16)
    plt.tick_params(axis='both', which='major',labelsize=16)
    plt.ylim(0,100)
    plt.savefig('death_valley_2014.png', bbox_inches='tight')
    plt.show()

filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date,'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    #print(highs)
    # Faz a plotagem dos dados
    fig = plt.figure(dpi=128, figsize=(10,6))
    plt.plot(dates, highs,c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue',alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='green', alpha=0.2)
    # Formata o gráfico
    title = 'Daily high and low temperatures - 2014\nDeath Valley, CA'
    plt.title(title, fontsize=20)
    plt.xlabel('', fontsize = 16)
    fig.autofmt_xdate()
    plt.ylabel('Temprature (F)',fontsize=16)
    plt.tick_params(axis='both', which='major',labelsize=16)
    plt.ylim(0, 100)
    plt.savefig('sitka_weather_2014.png', bbox_inches='tight')
    plt.show()
