import os
import csv

budget_data = os.path.join("Resources", "budget_data.csv")

# Lists to store data
Dates = []
Profits = []

#Initializing values at zero
TotalMonths = 0
TotalProfitsLoss = 0
value = 0
change = 0

with open(budget_data) as csvfile:
    name = csv.reader(csvfile, delimiter=',')
    next(name,None)
    for row in name:
        #Date
        Dates.append(row[0])

        #Adding up total months
        TotalMonths += 1

        #Profits/Losses
        Profits.append(int(row[1]))
        TotalProfitsLoss = TotalProfitsLoss + int(row[1])

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