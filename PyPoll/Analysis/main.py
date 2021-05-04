# Import modules
import os
import csv

candidate_count = {}  

# Path to collect data from the Resources folder
csvpath = os.path.join('..', 'Resources', 'election_data.csv')

# Read in the CSV file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # # Remove header from dataset
    csv_header = next(csvreader)
    data = list(csvreader)

    # set total votes to value of zero outside of for loop
    total_votes = 0

    # Loop through each row with  
    # https://www.w3schools.com/python/ref_func_enumerate.asp
for row in data: 
    enumerate(data)

    # add 1 to total votes
    total_votes += 1

    # assign candidate variable to 3rd row of csv
    candidate = row[2]

    # add 1 to candidate count for candidate variable if found more than once
    if candidate in list(candidate_count.keys()):
        candidate_count[candidate] += 1

    # otherwise the count for that candidate equals 1
    else:
        candidate_count[candidate] = 1

    # print the following for results variable:
    results = ""
    for candidate in list(candidate_count.keys()):
        candidate_percentage = (float(candidate_count[candidate]) / total_votes) * 100
        candidate_final = str(f"{candidate}: {round(candidate_percentage, 2)}% ({candidate_count[candidate]})")
        results += candidate_final
        
    # determine the winner of the race by identifying person with most votes added to their count
    for person in candidate_count.keys():
        if candidate_count[person] == max(candidate_count.values()):
            winner = person



printout = (
    "Election Results \n"
    "------------------------- \n"
    f"Total Votes: {total_votes} \n"
    "------------------------- \n"
    f"{results} \n"
    "------------------------- \n"
    f"Winner: {winner} \n"
    "------------------------- \n"
)

# print to terminal
print(printout)

#Create a .txt file with analysis
printout_file = open('printout_file.txt', 'w')

printout_file.write(printout)

printout_file.close()