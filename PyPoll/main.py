#modules
import os
import csv

#Path of CSV file
election_data = os.path.join("Resources", "election_data.csv")

#Lists to store data
candidate_list = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]

#Reading csv file
with open(election_data) as csvfile:
    name = csv.reader(csvfile, delimiter=',')
    next(name,None)

    #Initializing values of variables
    total_votes = sum(1 for row in name)

    #Starting for loop
    for row in name:
        #Candidate List
        candidate_list = row[2]

#Show On Screen Output
print('Election Results')
print('-----------------------------------------------------')
print(f'Total Votes: {total_votes}')
print('-----------------------------------------------------')