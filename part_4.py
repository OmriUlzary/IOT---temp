import numpy as np
import pandas as pd
from data_set import data

#1
print(data[data['temp'] == data['temp'].max()]["id"].sample())

#2
print(data[data['out/in'] == 'Out']['out/in'].count() / data[data['out/in'] == 'In']['out/in'].count())


#3
print(data[data['out/in'] == 'In']['out/in'].count() / data[data['out/in'] == 'Out']['out/in'].count())

#4
print(data[data['out/in'] == 'In']['temp'].mean())

#5
result_5 = data[data['out/in'] == 'Out']['temp']
print(result_5.mean())

#6
print(data.groupby('temp')['temp'].count())

#7
result_7 = data.groupby('temp')
groups_list = []
for name, group in result_7:
    groups_list.append(name)
print(groups_list)

#8
print(data[(data["temp"] >= 30) & (data["temp"] <= 37)].count())

#9
result_9 = data["temp"].value_counts().head(3)
print(result_9)


