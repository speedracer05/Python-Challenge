# pypoll
# ! The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.
# Final script should both print the analysis to the terminal and export a text file

import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

# Variables
total_votes = 0     # Set int value to zero
candidate_list = []
count_vlist = []
election_file = ["election_data.csv"]

# Set iteration through rows in election file
for file in election_file:
    
# Open file
    with open(csvpath, 'r') as file:
        file.readline()
        csvreader = csv.reader(file, delimiter=',')
# Iterate rows in csv, increment total votes list by 1 for each row
        for row in csvreader:
            total_votes = total_votes+1
            candidate = row[2]

print(total_votes)
print(candidate)