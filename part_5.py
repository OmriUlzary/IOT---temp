import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import part_4
from data_set import data

#8
group_8 = data.groupby(data[(data['temp'] > 29) & (data['temp'] < 39)]['temp'])
plot_8 = group_8['temp'].count().plot(kind='bar', color = 'pink')
plt.grid()
plt.xlabel('Temperature')
plt.ylabel('Rows')
plt.title('The numbers of rows 30-38 temperature')
plt.show(plot_8)

#4+5
groups_2 = data.groupby("out/in")
In = groups_2.get_group('In').count()['out/in']
Out = groups_2.get_group('Out').count()['out/in']
labels = 'In', 'Out'
sizes = In, Out
colors = ['lightcoral', 'lightskyblue']
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.title('The proportion between the temperatures measured inside or outside ')
plt.legend()


#5
meanpoint = dict(marker='D', markeredgecolor='black', markerfacecolor='firebrick')
plt.boxplot(part_4.result_5, meanprops=meanpoint, meanline=False, showmeans=True)
plt.ylabel('Temperature')
plt.title('Average temperatures measured outside')


#9
part_4.result_9.sort_values().plot(kind = 'bar', color = 'g')
plt.ylim([0, 10300])
plt.xlabel('Temperature')
plt.ylabel('Appearances')
plt.title('Top 3 appearance')
plt.vlines(-1, 0, 10500, colors = 'k', linestyles= 'dashed')
plt.vlines(3, 0, 10500, colors = 'k', linestyles= 'dashed')
plt.xlim(-2, 4)
plt.legend('③❸')

#6
y = (data.groupby("temp")["temp"])
count = (data.groupby("temp")["temp"].count())
y_pos = np.arange(21, 52)
plt.barh(y_pos, count, alpha = 0.9 )
plt.xlabel('Data amount')
plt.ylabel('Temperature')
plt.title('Data amount by temperature')
plt.legend()

plt.show()