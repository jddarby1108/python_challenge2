import os

import csv

from collections import Counter

csv_path = os.path.join('Resources', 'budget_data.csv')

contents = []
dates = []
pl = []

#Open and read csv
with open(csv_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    #Read the header row
    csv_header = next(csv_file)
    
    # append create lists and start formulas
    for row in csv_reader:
        dates.append(row[0])
        pl.append(float(row[1]))


        #    The total number of months included in the dataset
        date_count = len(list(dates))
        
        # the total of the profits and losses
        pl_total = sum(pl)

        # the average of the profits and losses
        pl_avg = pl_total / date_count

        # the greatest increase in profits and losses
        pl_max = max(pl)
        
        # the greatest decrease in profits and losses
        pl_min = min(pl)

        
        
# print all values to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {date_count}")
print(f"Total: $%5d" % (int(pl_total)))
print(f"Average Change: $%5d " % (int(pl_avg)))
print(f"Greatest Increase in Profits: $%5d" % (int(pl_max)))
print(f"Greatest Decrease in Profits: $%5d" % (int(pl_min)))


#export results to a text file
output_path = os.path.join("new.csv")

with open(output_path, 'w') as csvfile:

    # Initialize csv.writer and write to file new
    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow([f"Total Months:  {date_count}"])
    csvwriter.writerow([f"Total: $%5d" % (int(pl_total))])
    csvwriter.writerow([f"Average Change: $%5d " % (int(pl_avg))])
    csvwriter.writerow([f"Greatest Increase in Profits: $%5d" % (int(pl_max))])
    csvwriter.writerow([f"Greatest Decrease in Profits: $%5d" % (int(pl_min))])


# # Creates a tuple, a sequence of immutable Python objects that cannot be changed
# myTuple = ('Python', 100, 'VBA', False)
# print(myTuple)
