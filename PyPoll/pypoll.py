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
Voter_Count = 0


# Open file using csv module
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
#    print(csvreader)

        # Read the header row first (skip this step if there is now header)
#    csv_header = next(csvreader)
#    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
#    for row in csvreader:
#        print(row)

        # Exclude  header row
    next(csvreader, None)

    # Loop through data in the csv file
    for row in csvreader:

        # Count number of votes in column 0.
        Voter_Count = 0 + 1
        print('Number of voters:' + str(len(Voter_Count)))
