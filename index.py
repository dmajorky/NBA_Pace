import numpy as np
import pandas as pd
from pandas import ExcelFile
import matplotlib as mpl
import matplotlib.pyplot as plt

# imported csv file using read_csv function 
data = pd.read_csv('NBA_stats.csv')

# dropped rows where Pace was not recorded
data.drop([75,74,73,72,71,70,69,68,67,66,65,64,63,62,61,60,59,58,57,56,55,54,53,52,51,50,49],axis=0,inplace=True)

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

plt.plot()