#modules
import os
import csv

#Path of CSV file
budget_data = os.path.join("Resources", "budget_data.csv")

#Lists to store data
Profits = []
change_list = []
month_list = []

#Reading csv file
with open(budget_data) as csvfile:
    name = csv.reader(csvfile, delimiter=',')
    next(name,None)

    #Initializing values of variables
    TotalMonths = 0
    TotalProfitsLoss = 0
    LastProfit = 0

    #Starting for loop
    for row in name:
            #Date
            (row[0])

            #Adding up total months
            TotalMonths += 1
            month_list.append(row[0])

            #Profits/Losses
            Profits = (int(row[1]))
            TotalProfitsLoss = TotalProfitsLoss + int(row[1])

            #Calculating the change of monthly profits and losses
            change = Profits - LastProfit
            change_list.append(change)
            LastProfit = Profits

            #Calculating the greatest changes of the monthly profits and losses 
            incr_month = month_list[change_list.index(max(change_list))]
            greatest_incr = max(change_list)
            decr_month = month_list[change_list.index(min(change_list))]
            greatest_decr = min(change_list)

#finding average change
change_list.pop(0)
average = round(int(sum(change_list)) / int(len(change_list)), 2)

#Show On Screen Output
print('Financial Analysis')
print('-----------------------------------------------------')
print(f'Total Months: {TotalMonths}')
print(f'Total: ${TotalProfitsLoss}')
print(f'Average Change: ${average}')
print(f'Greatest Increase in Profits: {incr_month} (${greatest_incr})')
print(f'Greatest Deccrease in Profits: {decr_month} (${greatest_decr})')

#Output data to text file
with open('analysis/output.txt', 'w') as f:
    f.write('Financial Analysis\n')
    f.write('-----------------------------------------------------\n')
    f.write(f'Total Months: {TotalMonths}\n')
    f.write(f'Total: ${TotalProfitsLoss}\n')
    f.write(f'Average Change: ${average}\n')
    f.write(f'Greatest Increase in Profits: {incr_month} (${greatest_incr})\n')
    f.write(f'Total: {decr_month} (${greatest_decr})')