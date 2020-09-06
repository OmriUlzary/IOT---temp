import numpy as np
import pandas as pd
from data_set import data

#1
try:
    def calc_average(data_frame, col_name):
        sum = 0
        count = 0
        for value in data_frame[col_name]:
            count += 1
            sum += value
        return sum/count
except:
    print("The Data frame or the column name is not found")
#implement by pandas

try:
    def calc_average_pandas(data_frame, col_name):
        return data_frame[col_name].mean()
except:
    print("The Data frame or the column name is not found")
#2
try:
    def calc_std(data_frame, col_name):
        mean = calc_average(data_frame, col_name)
        N = 0
        X = 0
        for value in data_frame[col_name]:
            N += 1
            X += (value - mean) ** 2
        return (X/(N-1))**(0.5)
except:
    print("The Data frame or the column name is not found")

#implement by pandas
try:
    def calc_std_via_pandas(data_frame, col_name):
        return data_frame[col_name].std()
except:
    print("The Data frame or the column name is not found")
#3
try:
    def calc_variance(data_frame, col_name):
        return (calc_std(data_frame, col_name)) ** 2
except:
    print("The Data frame or the column name is not found")

#implement by pandas
try:
    def calc_variance_via_pandas(data_frame, col_name):
        return data_frame[col_name].var()
except:
    print("The Data frame or the column name is not found")
#4
try:
    def calc_mode(data_frame, co_name):
        column_dict = {}
        for i in data_frame[co_name]:
            if i in column_dict:
                column_dict[i] += 1
            else:
                column_dict[i] = 1
        max_number = 0
        for i in column_dict:
            if column_dict[i] > max_number:
                max_number = column_dict[i]
        mode_list = []
        for i in column_dict:
            if max_number == column_dict[i]:
                mode_list.append(i)
        return mode_list
except:
    print("The Data frame or the column name is not found")

#implement by pandas
try:
    def calc_mode_via_pandas(data_frame, co_name):
        return data_frame[co_name].mode()
except:
    print("The Data frame or the column name is not found")

#5
try:
    def calc_fx(data_frame,co_name):
        co_name_sorted = sorted(data_frame[co_name])
        average = calc_average(data_frame, co_name)
        std = calc_std(data_frame, co_name)
        fx_array = []
        for i in co_name_sorted:
            if i >= average:
                fx_array.append((i-average)/std)
            else:
                fx_array.append(i)
        return fx_array
except:
    print("The Data frame or the column name is not found")

try:
    def calc_i_fx(data_frame, co_name):
        sum = 0
        count = 1
        fx = calc_fx(data_frame, co_name)
        for i in fx:
            sum += count * i
            count += 1
        return sum
except:
    print("The Data frame or the column name is not found")

#according to pandas
try:
    X_pd = data['temp'].sort_values()
    mean_pd = X_pd.mean()
    std_pd = X_pd.std()
    above_the_mean = data[data['temp'] >= X_pd.mean()]['temp']
    normalization = above_the_mean.apply(lambda x:(x-mean_pd)/std_pd)
    below_the_mean = data[data['temp'] < X_pd.mean()]['temp']
    f_pd = below_the_mean.append(normalization)
except:
    print("The Data frame or the column name is not found")

#gx
try:
    def calc_gx(data_frame, co_name1, co_name2):
        zip_object = zip(data_frame[co_name1], data_frame[co_name2])
        gx_array = []
        gx_array_normalized = []
        for i, j in zip_object:
            if j == 'Out':
                gx_array.append(i)
        sorted_gx_array = sorted(gx_array)
        average = calc_average(data_frame, co_name1)
        std = calc_std(data_frame, co_name1)
        for i in sorted_gx_array:
            if i >= average:
                gx_array_normalized.append((i-average)/std)
            else:
                gx_array_normalized.append(i)
        return gx_array_normalized
except:
    print("The Data frame or the column name is not found")

try:
    def calc_sum_gx_fx(data_frame, co_name1, co_name2):
        return sum(calc_fx(data_frame,co_name1)) + sum(calc_gx(data_frame,co_name1,co_name2))
except:
    print("The Data frame or the columns name is not found")

#according to pandas
try:
    outside = data[data['out/in'] == 'Out']['temp'].sort_values()
    mean_pd = X_pd.mean()
    std_pd = X_pd.std()
    outside_above_the_mean = outside[outside >= X_pd.mean()]
    outside_normalization = outside_above_the_mean.apply(lambda x:(x-mean_pd)/std_pd)
    outside_below_the_mean = outside[outside < X_pd.mean()]
    g_pd = outside_below_the_mean.append(outside_normalization)
except:
    print("The Data frame or the column name is not found")





