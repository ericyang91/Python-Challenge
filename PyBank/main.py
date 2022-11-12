import os
import csv


def average(list):
    return sum(list)/len(list)

    # Defined a function that returns the average of a list.


pybankpath = os.path.join(r"C:/Users/ericj/Desktop/Challenges/Python-Challenge/PyBank", "Resources", "budget_data.csv")
# For reading the csv data
results = open("C:/Users/ericj/Desktop/Challenges/Python-Challenge/PyBank/Analysis/Analysis.txt", "w")
# For writing the results in txt

with open (pybankpath, 'r', encoding = 'utf') as pybankcsv:
    pybankreader = csv.reader(pybankcsv, delimiter=',')
    
    months = []
    # For counting the number of months in the data
    profit_losses = []
    # For calculating the net profit/loss
    net_pl_change = []
    # For calculating average net profit/loss change
    datelist = []
    # To be used as the value to the dictionary "roster"

    header = next(pybankreader)
    # Skip header
    first_row = next(pybankreader)
    # Skip the first row of data and at the same time assign the row to a variable

    previous_net = int(first_row[1])
    # For calculating the net change in profit/loss that will get appended to net_pl_change
    months.append(first_row[0])
    # Since we skipped the first row of data, appending the data manually to the list
    profit_losses.append(int(first_row[1]))
    # Since we skipped the first row of data, appending the data manually to the list

    for row in pybankreader:
        # The loop starts from the second data row after the header
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
# Zipped net_pl_change and datelist into a dictionary
greatest_increase = (max(net_pl_change))
greatest_increase_date = (roster[(max(net_pl_change))])
# Used the dictionary to find the corresponding date value
greatest_decrease = (min(net_pl_change))
greatest_decrease_date = (roster[(min(net_pl_change))])
# Used the dictionary to find the corresponding date value

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
results.write(f'The greatest decrease in profits was from {greatest_decrease_date} in the amount of ${greatest_decrease}.')