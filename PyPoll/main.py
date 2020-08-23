import os
import csv

from collections import Counter

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
form_string = []


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


        form_string = print(str(cand_name[index]) + ": " + str(vote_perc) + "%  (" + str(votes) + ")")

   
        
                

    
    
            
        
# # print all values to the terminal
# print("Election Results")
# print(spacer)
# print(f"Total Votes: {vote_count}")
# print(spacer)
        




# #export results to a text file
# output_path = os.path.join("new.csv")

# with open(output_path, 'w') as csvfile:

#     # Initialize csv.writer and write to file new
#     csvwriter = csv.writer(csvfile, delimiter=',')

#     csvwriter.writerow(["Election Results"]) 
#     csvwriter.writerow([spacer])
#     csvwriter.writerow([f"Total Votes: %5d " % (int(vote_count))])
#     csvwriter.writerow([spacer])
