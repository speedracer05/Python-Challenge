# The total number of months included in the dataset
    #split months from year, keying on " - "
# The net total amount of "Profit/Losses" over the entire period
# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

# csv file comma delimited, date profit/losses


import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

# List of variables
date = []
rev = []
rev_change = []
avg_change = []
profit_gain = []
profit_loss = []
total_rev = []

# Open file using csv module
with open(csvpath) as csvfile:
    # CSV reader specified delimiter and variable that holds the contents
    csvreader = csv.reader(csvfile, delimiter=',')

