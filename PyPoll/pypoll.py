# pypoll
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

# List of Variables
total_votes = []
candidates_list = []
unique_candidate = []
percentage_votes = []

# create empty counter
count = 0


# Open file using csv module
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

# Read header row
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Direct csvreader to skip the header and count number of lines in csv file
    if csv.Sniffer().has_header:
        next(csvreader)
    data = list(csvreader)
    total_votes = len(data)
print(f'There were a total of: {total_votes} votes')
