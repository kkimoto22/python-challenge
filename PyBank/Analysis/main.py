# Import modules
import os
import csv

# Define lists to which to add
months_column = []
# total_months = 0
profits_losses = []
# net_profits_losses = 0


# Path to collect data from the Resources folder
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

# Read in the CSV file
with open(csvpath, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # # Remove header from dataset and print header titles
    csv_header = next(csvreader)

    # Loop through each row 
    for row in csvreader:

        # Add to # of months
        months_column.append(row[0])
        # Add to profits/losses
        profits_losses.append(float(row[1]))

# Determine total months--indent?
total_months = len(months_column)

# Determine net profits/losses
net_profits_losses = sum(profits_losses)

# Determine average change of profits/losses over entire period
average_change = (net_profits_losses) / (total_months)

# Determine greatest increase in profits (date and amount) over the entire period
max_profit = max(profits_losses)

index_max_profit = profits_losses.index(max_profit)
max_month = months_column[index_max_profit]

# Determine greatest decrease in profits (date and amount) over the entire period
min_profit = min(profits_losses)

index_min_profit = profits_losses.index(min_profit)
min_month = months_column[index_min_profit]


analysis = (f'''Financial Analysis
----------------------------
Total Months: {total_months}
Net Total: {net_profits_losses: .2f}
Average Change: ${average_change: .2f}
Greatest Increase in Profits: {max_month} {max_profit: .2f}
Greatest Decrease in Profits: {min_month} {min_profit: .2f}''')

print(analysis)

#Create a .txt file with analysis
analysis_file = open('financial_analysis.txt', 'w')

analysis_file.write(analysis)

analysis_file.close()