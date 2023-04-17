#modules
import os
import csv

#Path of CSV file
election_data = os.path.join("Resources", "election_data.csv")

#Lists to store data
candidate_list = []
winnder = []


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
    for row in name:
            #Adding up total number of votes cast


            #complete list of candidates who received votes


            #The percentage of votes each candidate won


            #The total number of votes each candidate won


            #The winner of the election based on popular vote

#Show On Screen Output



#Output data to text file
