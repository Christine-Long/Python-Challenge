import os
import csv

# In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called budget_data.csv. The dataset is composed of two columns: Date and Profit/Losses. (Thankfully, your company has rather lax standards for accounting so the records are simple.)
budget_csv = os.path.join("C:/Users/Christine Long/Python-Challenge/PyBank/Resources/budget_data.csv")

# Your task is to create a Python script that analyzes the records to calculate each of the following:

#counters
totalmonths = 0
netamt = 0
previousval = 0
changelist = []
dates = []

#open csv file to read
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)

    firstval = next(csvreader)
    dates.append(firstval[0])
    netamt += int(firstval[1])
    previousval = int(firstval[1])

    for row in csvreader:

#add the dates into a list
        dates.append(row[0])     

# The net total amount of "Profit/Losses" over the entire period
        netamt += int(row[1])

# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
        change = int(row[1]) - previousval
        changelist.append(change)
        previousval = int(row[1])
    
    avgchange = round((sum(changelist) / len(changelist)),2)
        
# The total number of months included in the dataset    
    totalmonths = len(dates)

# The greatest increase in profits (date and amount) over the entire period
    greatest_increase = max(changelist)
    max_index = changelist.index(greatest_increase)
    max_date = dates[max_index]

# The greatest decrease in losses (date and amount) over the entire period
    greatest_decrease = min(changelist)
    min_index = changelist.index(greatest_decrease)
    min_date = dates[min_index]

#print the analysis
print(f'''
Financial Analysis
------------------
Total Months: {totalmonths}
Total: ${netamt}
Average Change: ${avgchange}
Greatest Increase in Profits: max_date $({greatest_increase})
Greatest Decrease in Profits: min_date $({greatest_decrease})
''')

#export to text file
output_path = os.path.join("C:/Users/Christine Long/Python-Challenge/PyBank/budget_text.txt")

with open(output_path, 'w', newline = '') as textfile:
    textfile.write(f'''
    Financial Analysis
    ------------------
    Total Months: {totalmonths}
    Total: ${netamt}
    Average Change: ${avgchange}
    Greatest Increase in Profits: max_date $({greatest_increase})
    Greatest Decrease in Profits: min_date $({greatest_decrease})
    ''')