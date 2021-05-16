# pypoll
# ! The total number of votes cast
# ! A complete list of candidates who received votes
# The percentage of votes each candidate won
# ! The total number of votes each candidate won
# The winner of the election based on popular vote.
# Final script should both print the analysis to the terminal and export a text file

import os
import csv
from types import GetSetDescriptorType

# Set path for file
csvpath = os.path.join('Resources', 'election_data.csv')

# List of Variables
total_votes = 0
candidate_list = []
candidate_count = {}
election_file = ['election_data.csv']
highest_votes = 0   # Set int value to zero for winning votes
# percent = []

# Iterate through rows in election file
for file in election_file:
    with open(csvpath, 'r') as file:
        csvreader = csv.reader(file, delimiter=',')
        csv_header = next(csvreader)
        # Iterate rows, increment total votes & get candidate name
        for row in csvreader:
            total_votes = total_votes+1
            candidate_name = row[2] 
            # Add unique candidate name & increment voter count
            if candidate_name not in candidate_list:
                candidate_list.append(candidate_name)
                candidate_count[candidate_name] = 0
            candidate_count[candidate_name] += 1
        for candidate_name in candidate_count:
            votes = candidate_count[candidate_name]
            percent = int(votes)/int(total_votes)*100
            candidate_results = (
                f'{candidate_name}: {percent:.1f}% ({votes:,})\n'
            )
        # winner = candidate_list[candidate_count.index(max(candidate_count))]

print(candidate_results)

outputpath = os.path.join('Analysis','Results.txt')


# Election Results
print('')
print('PyPoll Election Analysis')
print('-'*26)
print(f'Total Votes: {total_votes}')
print('-'*26)
# for row in range(len(candidate_list)):
#     print(f'{candidate_name[row]}: {percent[row]}% {votes[row]})\n'
#             )
# for row in range(len(candidate_list)):
#     print(f'{candidate_list[row]}: {percent[row]}% {candidate_count[row]}')
print(candidate_count)
print('-'*26)