import os
import csv


def average(list):
    return sum(list)/len(list)


pybankpath = os.path.join(r"C:/Users/ericj/Desktop/Challenges/Python-Challenge/PyBank", "Resources", "budget_data.csv")
results = open("C:/Users/ericj/Desktop/Challenges/Python-Challenge/PyBank/Analysis/Analysis.txt", "w")
with open (pybankpath, 'r', encoding = 'utf') as pybankcsv:
    pybankreader = csv.reader(pybankcsv, delimiter=',')
    months = []
    profit_losses = []
    net_pl_change = []
    datelist = []

    header = next(pybankreader)   
    first_row = next(pybankreader)

    previous_net = int(first_row[1])
    months.append(first_row[0])
    profit_losses.append(int(first_row[1]))
    
    for row in pybankreader:
        months.append(row[0])
        profit_losses.append(int(row[1]))
        net_change = int(row[1]) - previous_net
        net_pl_change.append(net_change)
        previous_net = int(row[1])
        datelist.append(row[0])

 

total_number_of_months = len(months)
net_total_profit_losses = sum(profit_losses)
average_PL_change = average(net_pl_change)

roster = dict(zip(net_pl_change, datelist))
greatest_increase = (max(net_pl_change))
greatest_increase_date = (roster[(max(net_pl_change))])
greatest_decrease = (min(net_pl_change))
greatest_decrease_date = (roster[(min(net_pl_change))])


print(f'The total number of months: {total_number_of_months}')
print(f'The net total amount of "Profit/Losses" over the entire period: {net_total_profit_losses}')
print(f'The average of changes in "Profit/Losses": {round(average_PL_change, 2)}')
print(f'The greatest increase in profits was from {greatest_increase_date} in the amount of ${greatest_increase}.')
print(f'The greatest decrease in profits was from {greatest_decrease_date} in the amount of ${greatest_decrease}.')

results.write('Financial Analysis\n')
results.write(f'The total number of months: {total_number_of_months}\n')
results.write(f'The net total amount of "Profit/Losses" over the entire period: {net_total_profit_losses}\n')
results.write(f'The average of changes in "Profit/Losses": {round(average_PL_change, 2)}\n')
results.write(f'The greatest increase in profits was from {greatest_increase_date} in the amount of ${greatest_increase}.\n')
results.write(f'The greatest decrease in profits was from {greatest_decrease_date} in the amount of ${greatest_decrease}.\n')

# * The greatest increase in profits (date and amount) over the entire period

# * The greatest decrease in profits (date and amount) over the entire period

#   Total Months: 86
#   Total: $22564198
#   Average Change: $-8311.11
#   Greatest Increase in Profits: Aug-16 ($1862002)
#   Greatest Decrease in Profits: Feb-14 ($-1825558)