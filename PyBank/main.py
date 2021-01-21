# PyBank

# Import modules
import os
import csv

# Define csv file path
budget_csv_path = os.path.join("Resources", "budget_data.csv")

# Open and read csv with defined delimiter
with open(budget_csv_path, 'r') as budget_file:
    budget_csv = csv.reader(budget_file, delimiter=",")

    # Read first row as header
    header = next(budget_csv)

    # Define months and profit_losses variables as lists
    months = []
    profit_losses = []

    # Set variables equal to 0 at start
    month_count = 0
    pl_net = 0
    pl_net_loop = 0
    pl_chg_net = 0
    pl_chg_loop = 0
    pl_chg_avg = 0
    pl_change = 0
    pl_chg_max = 0
    pl_chg_min = 0
    pl_chg_max_index = 0
    pl_chg_min_index = 0

    # Read each row of dataset csv and add to each assigned value
        # Assign column 0 as month values and column 1 as profitloss values
        # Add each row of month values from dataset to months list
        # Add each row of profitloss values from dataset to profit_losses list
    for row in budget_csv:
        month = row[0]
        profitloss = row[1]
        months.append(month)
        profit_losses.append(profitloss)

    # Calculate the total number of unique months by finding length of set of months list
    month_count = len(set(months))
    # Test
    # print(month_count)

    # Loop to calculate net total amount of "Profit/Losses" over entire period
    for pl_net_loop in range(month_count):
        pl_net = pl_net + int(profit_losses[pl_net_loop])
    # Test print with comma formatting
    # print(f"${pl_net:,}")

    # Calculate total changes in "Profit/Losses" over the entire period
    # Subtract 1 from month_count range so output so list index is not out of range (no change in first month)
    for pl_chg_loop in range(month_count - 1):
        pl_chg_net = pl_chg_net + (int(profit_losses[pl_chg_loop + 1]) - int(profit_losses[pl_chg_loop]))

        # Calculate average of changes over the entire period
        # Subtract 1 from month_count when finding average as well since there is no change in first month
        pl_chg_avg = (pl_chg_net / (month_count - 1))
        # Test print with comma formatting rounded to 2 decimal places
        # print(f"${pl_avg_change:,.2f}")

        # Calculate monthly "Profit/Losses" change
        pl_change = int(profit_losses[pl_chg_loop + 1]) - int(profit_losses[pl_chg_loop])

        # Find greatest increase in profits over the entire period
        # Need to add 1 to pl_chg_max_index because index will produce change start month but change is measured by end month
        if (pl_change > pl_chg_max):
            pl_chg_max = pl_change
            pl_chg_max_index = (pl_chg_loop + 1)
        else:
            pl_chg_max = pl_chg_max
    # Test
    # print(f"{months[pl_chg_max_index]} (${pl_chg_max:,})")

        # Find greatest decrease in losses over the entire period
        # Need to add 1 to pl_chg_min_index because index will produce change start month but change is measured by end month
        if (pl_change < pl_chg_min):
            pl_chg_min = pl_change
            pl_chg_min_index = (pl_chg_loop + 1)
        else:
            pl_chg_min = pl_chg_min
    # Test
    # print(f"{months[pl_chg_min_index]} (${pl_chg_min:,})")

# Print analysis results to terminal
analysis_results = (f"\
Financial Analysis\n\
----------------------------\n\
Total Months: {month_count}\n\
Total: ${pl_net:,}\n\
Average  Change: ${pl_chg_avg:,.2f}\n\
Greatest Increase in Profits: {months[pl_chg_max_index]} (${pl_chg_max:,})\n\
Greatest Decrease in Profits: {months[pl_chg_min_index]} (${pl_chg_min:,})\n"
)

print(analysis_results)

# Export analysis results to text file
output_path = os.path.join("PyBank_Analysis", "PyBank_analysis_results.txt")
with open(output_path, "w") as PyBank_txt:
    PyBank_txt.write(analysis_results)