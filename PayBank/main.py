'-*- coding: UTF-8 -*-'
"""PyBank_Homework Starter File"""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
value = 0
change = 0
dates = []
profits = []

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    
    total_months += 1
    total_net += int(first_row[1])
    value = int(first_row[1])

    # Process each row of data
    for row in reader:
        dates.append(row[0])  # Assuming the first column is the date
        total_months += 1
        total_net += int(row[1])
        
        change = int(row[1]) - value
        profits.append(change)
        value = int(row[1])

    # Calculate the greatest increase in profits (month and amount)
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]

    # Calculate the greatest decrease in losses (month and amount)
    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]

# Calculate the average net change across the months
avg_change = sum(profits) / len(profits)

# Generate the output summary
output = (
    "Financial Analysis\n"
    "---------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${round(avg_change, 2)}\n"
    f"Greatest Increase in Profits: {greatest_date} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {worst_date} (${greatest_decrease})\n"
)

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)