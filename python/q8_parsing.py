# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import numpy as np

with open('football.csv','r') as f:
    lines = []
    for line in f:
        lines.append(line.split(','))

ind_team, ind_goals, ind_allowed = lines[0].index('Team'), lines[0].index('Goals'), lines[0].index('Goals Allowed')

list_teams = [line[ind_team] for line in lines[1:]] 
list_goals = [int(line[ind_goals]) for line in lines[1:]]
list_allowed = [int(line[ind_allowed]) for line in lines[1:]]

goal_diffs = [abs(goals-allowed) for goals, allowed in zip(list_goals, list_allowed)]
ind_min_dif = np.argmin(goal_diffs)

print("The team with the smallest difference in 'for' and 'against' goals is: %s" % list_teams[ind_min_dif])
