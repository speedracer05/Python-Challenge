#PyPoll

#You will be give a set of poll data called election_data.csv. The dataset is composed of 
# three columns: Voter ID, County, and Candidate. Your task is to create a Python script that 
# analyzes the votes and calculates each of the following:

    # The total number of votes cast
    # A complete list of candidates who received votes
    # The percentage of votes each candidate won
    # The total number of votes each candidate won
    # The winner of the election based on popular vote.

import os
import csv

# Set path for file
#csvpath = os.path.join("C:\Users\jchan\Documents\UCD_bootcamp\Python-Challenge\PyPoll\Resources\"election_data.csv")

with open(csvpath, newline='') as csv_file:
    reader = csv.reader(csv_file, delimiter=',',)
    for row in reader:
        print(row)

# List of variables
#Candidate
#Khan
#Correy
#Li
#O'Tooley
