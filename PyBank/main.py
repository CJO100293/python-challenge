#modules
import os
import csv

#Path of CSV file
budget_data = os.path.join("Resources", "budget_data.csv")

#Lists to store data
Profits = []

#Reading csv file
with open(budget_data) as csvfile:
    name = csv.reader(csvfile, delimiter=',')
    next(name,None)

    #Initializing values of variables
    TotalMonths = 0
    TotalProfitsLoss = 0

    #Starting for loop
    for row in name:
            #Date
            (row[0])

            #Adding up total months
            TotalMonths += 1

            #Profits/Losses
            Profits.append(int(row[1]))
            TotalProfitsLoss = TotalProfitsLoss + int(row[1])

            #Calculating the average change of monthly profits and losses

            #Calculating the greatest changes of the monthly profits and losses 

#Show On Screen Output
print('Financial Analysis')
print('-----------------------------------------------------')
print(f'Total Months: {TotalMonths}')
print(f'Total: ${TotalProfitsLoss}')

#Output data to text file
with open('analysis/output.txt', 'w') as f:
    f.write('Financial Analysis\n')
    f.write('-----------------------------------------------------\n')
    f.write(f'Total Months: {TotalMonths}\n')
    f.write(f'Total: ${TotalProfitsLoss}\n')