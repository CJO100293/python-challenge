#modules
import os
import csv

#Path of CSV file
election_data = os.path.join("Resources", "election_data.csv")

#Lists to store data
candidate_list = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
candidate_votes = [0,0,0]

#Reading csv file
with open(election_data) as csvfile:
    name = csv.reader(csvfile, delimiter=',')
    next(name,None)

    #Initializing values of variables
    total_votes = 0

    #Starting for loop
    for row in name:
        #Counting Total Votes
        total_votes = total_votes + 1
        #Candidate List + calculating total votes per candidate
        if candidate_list[0] == row[2]:
            candidate_votes[0] += 1
        if candidate_list[1] == row[2]:
            candidate_votes[1] += 1
        if candidate_list[2] == row[2]:
            candidate_votes[2] += 1

#Show On Screen Output
print('Election Results')
print('-----------------------------------------------------')
print(f'Total Votes: {total_votes}')
print('-----------------------------------------------------')
print(f'{candidate_list[0]}: more stuff here ({candidate_votes[0]})')
print(f'{candidate_list[1]}: more stuff here ({candidate_votes[1]})')
print(f'{candidate_list[2]}: more stuff here ({candidate_votes[2]})')
print('-----------------------------------------------------')