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
