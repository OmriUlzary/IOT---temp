import numpy as np
import pandas as pd
from data_set import data

#2
X, Y = data.shape

print("Number of rows: " + str(X) + "\nNumber of cols: " + str(Y))

#3
print(list(data.columns))

#4
data_statistic = data["temp"].describe()
sum_temp = data["temp"].sum()
median_temp = data["temp"].median()
max_temp = data["temp"].max()
print(data_statistic[:4])
print("Max  " + str(max_temp))
print("Sum  " + str(sum_temp))
print("Median  " + str(median_temp))

#5
range_temperature = data["temp"].max() - data["temp"].min()
print("Range  " + str(range_temperature))