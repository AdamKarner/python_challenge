# Modules used
import os
import csv


## Path to the source .csv file
csvpath = os.path.join("Resources", "budget_data.csv")


### Main Variables
total_months = 0
net_profit_loss = 0
prev_row_profit_loss = None


#### Lists to store data
Month=[]
PL_Change=[]


###### Open and read file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Set the header row to skip it in the loop
    header = next(csvreader)


    ## Loop through each row. Extract Months and profit/loss value from the row and store
    for row in csvreader:
        month = row[0] #sets the variable for the month as the value in the 1st column of the csv file
        profit_loss = int(row[1])

        #add 1 to the total months counter
        total_months +=1
        #add the profit and loss value to the total profit and loss counter
        net_profit_loss +=profit_loss
        #if the previous row profit and loss variable is not empty, calculate the change in profit and loss and add that amount and the correcsponding month to their lists for later reference.
        if prev_row_profit_loss is not None:
            change = profit_loss - prev_row_profit_loss
            PL_Change.append(change)
            Month.append(month)
        #update the prev_row_profit_loss variable
        prev_row_profit_loss = profit_loss


####### Create results variables using their calculation methods
avg_change = sum(PL_Change)/ (total_months-1)
most_pl_change = max(PL_Change)
most_pl_month = Month[PL_Change.index(most_pl_change)]
least_pl_change = min(PL_Change)
least_pl_month = Month[PL_Change.index(least_pl_change)]


######## Format output and assign it to a variable. Limit average change result to only 2 decimal places. Add $ symbols and () where needed per output format instructions
Results = (
    "Financial Analysis\n"                                  
    "----------------------\n"                                
    f"Total Months: {total_months}\n"
    f"Total: ${net_profit_loss}\n"
    f"Average Change: ${avg_change:.2f}\n"
    f"Greatest Increase in Profits: {most_pl_month} (${most_pl_change})\n"
    f"Greatest Decrease in Profits: {least_pl_month} (${least_pl_change})\n")


######### Print in terminal
print(Results)


######### Output file as .txt file to the analysis folder
output_path = os.path.join("analysis", "PyBank_Results.txt")
with open(output_path, "w") as textfile:
    textfile.write(Results)


#  I did have to lookup how to get the data to print on the .txt file on separate lines and learned I could have done the terminal output that way and assigned it a variable so I could reference
# the entire results output. My original print commands were:

            # print("Financial Analysis")
            # print("Financial Analysis")
            # print("---------------------------------------------")
            # print(f"Total Months: {total_months}")
            # print(f"Average Change: ${avg_change:.2f} ")
            # print(f"Greatest Increase in Profits: {most_pl_month} (${most_pl_change})")
            # print(f"Greatest Decrease in Profits: {least_pl_month} (${least_pl_change})")

            # ######### Output file as .txt file to the analysis folder
            # output_path = os.path.join("analysis", "PyBank_Results.txt")
            # with open(output_path, "w") as textfile:
            #     textfile.write(
            #         "Financial Analysis\n"                                  
            #         "----------------------\n"                                
            #         f"Total Months: {total_months}\n"
            #         f"Average Change: ${avg_change:.2f}\n"
            #         f"Greatest Increase in Profits: {most_pl_month} (${most_pl_change})\n"
            #         f"Greatest Decrease in Profits: {least_pl_month} (${least_pl_change})\n"
            #     )
