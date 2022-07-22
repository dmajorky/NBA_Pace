import numpy as np
import pandas as pd
from pandas import ExcelFile
import matplotlib as mpl
import matplotlib.pyplot as plt

#imported csv file using read_csv function
data = pd.read_csv('NBA_stats.csv')

# dropped rows where Pace was not recorded
data.drop(range(27),axis=0,inplace=True)

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
plt.plot(data['Season'],data['Pace'])
plt.title("NBA Pace Throughout History")
plt.xlabel("Season")
plt.ylabel("Pace")
plt.xticks(rotation = 90)
plt.show()

#scatter plot showing strong correlation between pace and points per game
plt.scatter(data['Pace'], data['PTS'])
plt.xlabel('Pace')
plt.ylabel('Points Per Game')
plt.title('Pace vs Points per Game')
plt.show()

#scatter plot showing little correlatio between pace and 3 pointers made per game
plt.scatter(data['Pace'], data['3P'])
plt.xlabel('Pace')
plt.ylabel('3 Pointers Made Per Game')
plt.title('Pace vs 3 Pointers Made Per Game')
plt.show()

#scatter plot showing strong correlation between pace and shots made per game
plt.scatter(data['Pace'], data['FG'])
plt.xlabel('Pace')
plt.ylabel('Shots Made Per Game')
plt.title('Pace vs Shots Made per Game')
plt.show()