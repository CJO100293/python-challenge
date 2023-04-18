#modules
import os
import csv

#Path of CSV file
election_data = os.path.join("Resources", "election_data.csv")

#Lists to store data
candidate_list = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
candidate_votes = [0,0,0]
votes_percent = [0,0,0]

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
#Calculating percentage of votes won for each candidate
votes_percent[0] = "{:.3f}".format((candidate_votes[0] / total_votes)*100)
votes_percent[1] = "{:.3f}".format((candidate_votes[1] / total_votes)*100)
votes_percent[2] = "{:.3f}".format((candidate_votes[2] / total_votes)*100)

#Calculating the winner
winner = max(candidate_votes)
winnerindex = candidate_votes.index(winner)
greatest_votes = candidate_list[winnerindex]

#Show On Screen Output
print('Election Results')
print('-----------------------------------------------------')
print(f'Total Votes: {total_votes}')
print('-----------------------------------------------------')
print(f'{candidate_list[0]}: {votes_percent[0]}% ({candidate_votes[0]})')
print(f'{candidate_list[1]}: {votes_percent[1]}% ({candidate_votes[1]})')
print(f'{candidate_list[2]}: {votes_percent[2]}% ({candidate_votes[2]})')
print('-----------------------------------------------------')
print(f'Winner: {greatest_votes}')
print('-----------------------------------------------------')

#Output data to text file
with open('analysis/output.txt', 'w') as f:
    f.write('Election Results\n')
    f.write('-----------------------------------------------------\n')
    f.write(f'Total Votes: {total_votes}\n')
    f.write('-----------------------------------------------------\n')
    f.write(f'{candidate_list[0]}: {votes_percent[0]}% ({candidate_votes[0]})\n')
    f.write(f'{candidate_list[1]}: {votes_percent[1]}% ({candidate_votes[1]})\n')
    f.write(f'{candidate_list[2]}: {votes_percent[2]}% ({candidate_votes[2]})\n')
    f.write('-----------------------------------------------------\n')
    f.write(f'Winner: {greatest_votes}\n')
    f.write('-----------------------------------------------------')