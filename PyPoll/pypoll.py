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

# List of Variables
total_votes = 0     # Set int value to zero
candidate_list = [] # Set empty list for candidate
candidate_count = []
count_vlist = []    # Set empty list for voter count
election_file = ["election_data.csv"]
highest_votes = 0   # Set int value to zero for winning votes
percent = []

# Set iteration through rows in election file
for file in election_file:
    
# Open file
    with open(csvpath, 'r') as file:
        file.readline()
        csvreader = csv.reader(file, delimiter=',')
# Iterate rows in csv, increment total votes list by 1 for each row
        for row in csvreader:
            total_votes = total_votes+1
            candidate_name = row[2]
# Populate candidate list with unique candidate names, then increment voter count list by 1
            if not candidate_name in candidate_list:
                candidate_list.append(candidate_name)
                count_vlist.append(1)
            
            # else:
            #     vote_sum = candidate_list.index(candidate_name)
            #     pointer_candidate = count_vlist[vote_sum]
            #     count_vlist[vote_sum] = vote_sum

print(total_votes)
print(candidate_list)
# print(count_vlist)
# print(str(total_votes))

for candidate_name in candidate_list:
    candidate_count.append((total_votes.count(candidate_name))
    percent.append(round(total_votes.count(candidate_name)/total_votes*100,3))

# for candidate_name in candidate_list:
#     votes = count_vlist[candidate_list.index(candidate_name)]
#     # print(votes)
#     vote_percent = (votes/total_votes)*100
