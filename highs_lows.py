import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    # 阅读器对象
    reader = csv.reader(f)
    header_row = next(reader)
    dates = []
    highs = []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        high = int(row[1])
        highs.append(high)
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)
    print(highs)
# 绘制画布
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.title("Daily high temperatures", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
fig.autofmt_xdate()
plt.plot(dates, highs, c="red")
plt.show()
