# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# Calculate the changes in "Profit/Losses" over the entire period, then find 
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
rev_change = [0]  # is list # change
sum_change = 0 # variable, set to zero # change sum
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
for r in range(0, len(rev)-1): # <-1> subtract one row for the header

    # Perform calculation to find the revenue change, from row r=1 from r.
    rev_change.append(int(rev[r+1]) - int(rev[r]))
    # print(rev_change)

# forLoop in the list rev_change, from zero to the end of items in rev_change
for c in range(0, len(rev_change)):
    
    # find the greatest gain
    if rev_change[c] > rev_gain:
        rev_gain = rev_change[c]

    # find the greatest decrease
    if rev_change[c] < rev_decrease:
        rev_decrease = rev_change[c]

    # total_rev is assigned an integer value of rev in list r
    total_rev = total_rev + int(rev[c])

    # Calculate the change in revenue (profit/loss). 
    sum_change = sum_change + (rev_change[c])

# Calculate the avg change.
AvgChange = int(sum_change / (len(rev_change)-1))

# Analysis print via Terminal
print("")
print("PyBank Financial Analysis")
print("**************************")
print("Total Months: " + str(len(date)))
print("Total Revenue: $" + str(total_rev))
print("Average Revenue Change: $" + str(AvgChange))
print("Greatest Increase in Profit: " + date[rev_change.index(rev_gain)] + " ($" + str(rev_gain) + ")")
print("Greatest Decrease in Profit: " + date[rev_change.index(rev_decrease)] + " ($" + str(rev_decrease) + ")")

# Write text file with results of financial analysis 4-9-2021 12:12AM
with open("Report_PyBank.txt", "w") as text_file:
    text_file.write("PyBank Financial Analysis" + "\n")
    text_file.write("**************************" + "\n")
    text_file.write("Total Months: " + str(len(date)) + "\n")
    text_file.write("Total Revenue: $" + str(total_rev) + "\n")
    text_file.write("Average Revenue Change: $" + str(AvgChange) + "\n")
    text_file.write("Greatest Increase in Profit: " + date[rev_change.index(rev_gain)] + " ($" + str(rev_gain) + ")" + "\n")
    text_file.write("Greatest Decrease in Profit: " + date[rev_change.index(rev_decrease)] + " ($" + str(rev_decrease) + ")")