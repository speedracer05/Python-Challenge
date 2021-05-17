import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

# List of variables
date = []
rev = []
rev_change = [0]
sum_change = 0
rev_gain = 0
rev_decrease = 0
total_rev = 0

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    for row in csvreader:
        date.append(row[0])
        rev.append(row[1])

for r in range(0, len(rev)-1):
    rev_change.append(int(rev[r+1]) - int(rev[r]))

for c in range(0, len(rev_change)):
    if rev_change[c] > rev_gain:
        rev_gain = rev_change[c]

    if rev_change[c] < rev_decrease:
        rev_decrease = rev_change[c]

    total_rev = total_rev + int(rev[c])
    sum_change = sum_change + (rev_change[c])

AvgChange = int(sum_change / (len(rev_change)-1))

outputpath = os.path.join('analysis','Results.txt')
results = open(outputpath, 'w')

export = []
export.append("")
export.append("PyBank Financial Analysis")
export.append("**************************")
export.append("Total Months: " + str(len(date)))
export.append("Total Revenue: $" + str(total_rev))
export.append("Average Revenue Change: $" + str(AvgChange))
export.append("Greatest Increase in Profit: " + date[rev_change.index(rev_gain)] + " ($" + str(rev_gain) + ")")
export.append("Greatest Decrease in Profit: " + date[rev_change.index(rev_decrease)] + " ($" + str(rev_decrease) + ")")
for line in export:
    print(line)
    print(line,file=results)
results.close()