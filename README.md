# NBA Pace Analysis

This project is an analysis of NBA pace throughout the history of the NBA. Pace is the average number of possessions a team has per game, which is a stat the NBA started 
to record in the 1973-74 season. I myself am a huge fan of the game of basketball and the NBA, so I follow the league very closely. 

I have been watching the NBA since 2006 and have noticed a lot of changes in how the game was being played. One of the most noticeable changes I saw was the 
speed in which the game was being played. From 2006 to about 2013-14 I noticed that the game was played at a slow pace mainly through the low post, and teams would 
often score less than 100 points a game. Then I started to see a change in the speed at which the game was played. It was no longer being played through the low post, 
teams were scoring over 100 points per game, and more 3 point shots were being made, as well as all shots overall. 

I looked at the data and noticed that pace was one stat the increased for the most part every year since 2006. So I wanted to see just how much of an impact pace has had 
throughout NBA history on points per game, shots made, and 3 pointers made, as well as if having a faster pace leads to a team winning a championship. 

# What needs to be installed

pip install numpy 

pip install pandas 

pip install matplotlib

import numpy as np

import pandas as pd

from pandas import ExcelFile

import matplotlib as mpl

import matplotlib.pyplot as plt

# Features included

Read in two csv files using the read_csv function

Used pandas drop() function to drop rows where pace was not recorded and to drop columns that were irrelevent 

Used 5 different pandas functions to do basic calculations by 
1. using the mean() function to find the average overall pace in NBA history
2. the min() to find the lowest recorded pace
3. the max() function to find the highest recorded pace
4. the corr() function to find the correlation between Pace & points per game (PTS), 3 pointers made(3P), 
and shots made(FG) per game
5. the describe() function to find the statistical summary of the data

Matplotlib to plot a line graph showing pace throughout NBA history as well as 3 scatter plots that shows the correlation between Pace, Points per game, Shots made per game, and 3 pointers made per game.  

# What I found

After analyzing the data I was able to find out that the NBA had a very high pace in the 1970s and 1980s. In fact the highest recorded pace was 107.8 in the 1973-74 season which was the very first year pace was recorded. Pace dropped continuously in the 1990s and the lowest pace was recorded at 88.9 in the 1998-99 season. 
The following season pace increased above 90 and stayed in the low 90s during the 2000s. It wouldn't be until 2015-16 until we saw a noticable change in pace, as it reached it's highest point since the mid 90s at 95.8. Pace would continue to climb, peaking at 100.3 in the 2019-20 season. 

According to the data pace has a very strong correlation to shots made per game (FG) and points per game (PTS). Both scatter plots show that the higher the average pace, the higher both points per game and shots made will be. However the same can not be said about 3 pointers made per game (3P). The data shows that there is no correlation betweeen pace and 3s made per game. But I think this can be explained pretty easily. The 3 point line was not introduced until the 1979-80 season, which means pace was being recorded 6 years before a 3 pointer was ever taken in the NBA. So this could skew the numbers a bit. Also the 3 point shot wasn't really a big part of most teams game plans until recently. In fact the league averge of 3 pointers made did not hit double digits until the 2018-19 at 10.3 3 pointers made per game. 

I took data from the past 11 NBA champions, from 2012-13 to 2021-22, to see if a team having a higher pace per game in the regular season leads to the ultimate goal of winning a championship. The data says that pace is not a good indicator of who will win a championship. In fact only 36.4% of teams that went on to win the championship had a pace ranked in the top 5 during this time span. 45.5% finished the season ranked between 19-11, and 18.2% were ranked 30-20. Pace may indicate that a team scores more points and makes more shots but it does not indicate team success in terms of championships.  
