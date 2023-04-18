#modules
import os
import csv

#Path of CSV file
election_data = os.path.join("Resources", "election_data.csv")

#Lists to store data
candidate_list = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
winner = []


#Reading csv file
with open(election_data) as csvfile:
    name = csv.reader(csvfile, delimiter=',')
    next(name,None)

    #Initializing values of variables
    total_votes = 0
    percentage = 0
    candidate_total_votes = 0
    candidate_win_votes = 0

    #Starting for loop
