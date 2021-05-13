# pypoll

import os
import csv

# Set path for file
csvpath = os.path.join(C:\Users\jchan\Documents\UCD_bootcamp\Python-Challenge\PyPoll\"election_data.csv")

# Open file using csv module
with open(csvpath, newline='') as csvfile: # might need to add ''in place of..., after "="
    # CSV reader specified delimiter and variable that holds the contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
    