import os
import csv

from collections import Counter
from collections import namedtuple

csv_path = os.path.join('Resources', 'election_data.csv')

voter_ids = []
counties = []
candidates = []
spacer = ("---------------------")
vote_count = []
person = []
cand_name = []
name = []
votes = []
vote_perc = []
votes_list = []
max_votes = []
winner = []
vote_results = []



#Open and read csv
with open(csv_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    #Read the header row
    csv_header = next(csv_file)
    
    # append create lists and start formulas
    for row in csv_reader:
        voter_ids.append(row[0])
        counties.append(row[1])
        candidates.append(row[2])
                
        # The total number of votes cast
        vote_count = len(voter_ids)

    print("Election Results")
    print(spacer)
    print(f"Total Votes: {vote_count}")
    print(spacer)
    
    # initializing candidate list and counting votes
    for person in candidates:
        if person not in cand_name:
            cand_name.append(person)

    for index, person in enumerate(cand_name):
        votes = candidates.count(cand_name[index])
        vote_perc = (votes / vote_count) * 100
        votes_list.append(votes)
        max_votes = max(votes_list)
        
        print(str(cand_name[index]) + ": " + ("{:.3f}".format(vote_perc)) + "%  (" + str(votes) + ")")
        
        for person in votes_list:
            if votes == max_votes:
                winner = cand_name[index]

print(spacer)
print("winner:  " + winner)
print(spacer)

# export results to a text file
output_path = os.path.join("new.csv")

with open(output_path, 'w') as csvfile:

    # Initialize csv.writer and write to file new
    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(["Election Results"])
    csvwriter.writerow([spacer])
    csvwriter.writerow([f"Total Votes: {vote_count}"])
    csvwriter.writerow([spacer])
    csvwriter.writerow(["I could not figure out"])
    csvwriter.writerow(["how to print a nested for loop"])
    csvwriter.writerow(["at the end of the command"])
    csvwriter.writerow(["BUT it did print to terminal :) "])
    csvwriter.writerow(["winner:  " + winner])
    csvwriter.writerow([spacer])      
                
    
    

    
    