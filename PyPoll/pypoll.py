import os
import csv

# Set path for csv & declare var
csvpath = os.path.join('Resources', 'election_data.csv')
total_votes = 0
votes = []
candidate_list = []
candidate_count = {}
candidate_tally = []
election_file = ['election_data.csv']
percent = []

# Get vote total, unique candidates, increment vote for ea candidate,
# calculate vote tally & percent, and determine winner
for file in election_file:
    with open(csvpath, 'r') as file:
        csvreader = csv.reader(file, delimiter=',')
        csv_header = next(csvreader)
        for row in csvreader:
            total_votes = total_votes+1
            candidate_name = row[2] 
            if candidate_name not in candidate_list:
                candidate_list.append(candidate_name)
                candidate_count[candidate_name]=0
            candidate_count[candidate_name]+=1
            votes.append(row[2])
        for candidate_name in candidate_count:
            percent.append(round(votes.count(candidate_name)/total_votes*100,3))
            candidate_tally.append(votes.count(candidate_name))
        winner = max(candidate_count, key=candidate_count.get)

outputpath = os.path.join('Analysis','Results.txt')
results = open(outputpath, 'w')

export = []
export.append('Election Results')
export.append('-'*26)
export.append(f'Total Votes: {total_votes}')
export.append('-'*26)
[export.append(f'{candidate_list[row]}: {percent[row]}% ({candidate_tally[row]})')
for row in range(len(candidate_list))
]
export.append('-'*26)
export.append(f'Winner: {winner}')
export.append('-'*26)
for line in export:
    print(line)
    print(line,file=results)
results.close()