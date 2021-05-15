# pypoll
# ! The total number of votes cast
# ! A complete list of candidates who received votes
# The percentage of votes each candidate won
# ! The total number of votes each candidate won
# The winner of the election based on popular vote.
# Final script should both print the analysis to the terminal and export a text file

import os
import csv

# Set path for file
csvpath = os.path.join('Resources', 'election_data.csv')

# List of Variables
total_votes = 0
candidate_list = []
candidate_count = {}
election_file = ['election_data.csv']
highest_votes = 0   # Set int value to zero for winning votes
percent = []

# Iterate through rows in election file
for file in election_file:
    
    # Open file
    with open(csvpath, 'r') as file:
        csvreader = csv.reader(file, delimiter=',')
        csv_header = next(csvreader)
        # Iterate rows, increment total votes list by 1 & get candidate name
        for row in csvreader:
            total_votes = total_votes+1
            candidate_name = row[2] 
            # Add unique candidate names, and increment voter count list by 1
            if candidate_name not in candidate_list:
                candidate_list.append(candidate_name)
                candidate_count[candidate_name] = 0
            candidate_count[candidate_name] += 1



print()
print(candidate_list)
print(candidate_count)


outputpath = os.path.join('Analysis','Results.txt')

resultsfile = open(outputpath, 'w')

# Election Results
print('')
print('PyPoll Election Analysis')
print('-'*26)
print(f'Total Votes: {total_votes}')
print('-'*26)
