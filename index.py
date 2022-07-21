import numpy as np
import pandas as pd
from pandas import ExcelFile
import matplotlib as mpl
import matplotlib.pyplot as plt

#imported csv file using read_csv function
data = pd.read_csv('NBA_stats.csv')

# dropped rows where Pace was not recorded
data.drop([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26],axis=0,inplace=True)

# dropped columns that were irrelevant
data.drop(['Rk','Lg','Age','Ht','Wt','G','MP','eFG%','TOV%','ORB%','FT/FGA','ORtg'],axis=1,inplace=True)

print(data)

# found the average pace in NBA history
mean_data = data['Pace'].mean()

print(mean_data)

# found lowest pace(min) & highest pace(max) in NBA history
min_data = data['Pace'].min()
max_data = data['Pace'].max()

print(min_data)
print(max_data)

#found correlation between Pace and PTS

print(data['Pace'].corr(data['PTS']))

#found correlation between Pace and 3P

print(data['Pace'].corr(data['3P']))

#found correlation between Pace and FG

print(data['Pace'].corr(data['FG']))

#found statistical summary of data 
print(data.describe())

# line graph of Pace throughout NBA history
data['Pace'].plot()
plt.title("NBA Pace Throughout History")
plt.xlabel("Season")
plt.ylabel("Pace")
plt.show()