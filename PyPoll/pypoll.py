# pypoll

import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

# Open file using csv module
with open(csvpath, newline='') as csvfile: # might need to add ''in place of..., after "="
    # CSV reader specified delimiter and variable that holds the contents
    csvreader = csv.reader(csvfile, delimiter=',')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

        # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)
