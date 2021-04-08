#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#Calculate the changes in "Profit/Losses" over the entire period, then find 
#  the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period

#The final script should both print the analysis to the terminal and export a 
#  text file with the results.

import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

# List of variables
date = []         # is list
rev = []          # is list
rev_change = [0]  # is list
avgrev_change = 0 # variable, set to zero
rev_gain = 0      # variable, set to zero
rev_decrease = 0  # variable, set to zero
total_rev = 0     # variable, set to zero

# Open file using csv module
with open(csvpath, newline='') as csvfile: # might need to add ''in place of..., after "="

    # CSV reader specified delimiter and variable that holds the contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Exclue  header row
    next(csvreader, None)

    # Loop through data in the csv file
    for row in csvreader:

        # date list in column 0 (actually 1). Data in each row is appended to the list
        date.append(row[0])
        # revenue list in column 1 (actually 2). Revenue in each row is appended to the list
        rev.append(row[1])

# Calculate the change in revenue over the entire period, and write to the list[rev-change]
for r in range(0, len(rev)-1):

    rev_change.append(int(rev[r+1]) - int(rev[r]))
    #print(rev_change)
    # manual validation for 1st calc checks out with terminal print: 984655-867884 = 116771