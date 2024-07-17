# Modules used
import os
import csv

## Path to Source .csv file
csvpath = os.path.join("Resources", "election_data.csv")


### Main Variables & Dictionary
total_votes = 0
Candidates ={}


#### Open and read file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Set the header row to skip it in the loop
    header = next(csvreader)
    
    ## Loop through each row. Count the number of votes and extract Candidate names and appearance counts. 
    for row in csvreader:
        total_votes +=1     #add 1 to the total votes count for each loop
        candidate = row[2]  #sets the variable for counting the candidates votes as the value in the 3rd column of the csv file
         
        if candidate in Candidates:
            Candidates[candidate] +=1 # if a value in the candidate column is present in the dictionary, add 1 to its total.
        else:
            Candidates[candidate] = 1 # if the value is not present in the dictionary, add the value and set its count to 1

##### Find the winner
winner = max(Candidates, key=Candidates.get)

###### Prepare the output result by assigning it to a variable
output_result = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
)

####### Calculate total votes per candidate and percentage and add each one to the output result
for candidate, votes in Candidates.items():
    vote_percentage = (votes / total_votes) * 100
    output_result+= f"{candidate}: {vote_percentage:.2f}% ({votes})\n"

######## Add the end of the output result
output_result += (
    "-------------------------\n"
    f"Winner: {winner}\n"
    "-------------------------"
)

######### Print in terminal 
print(output_result)

########## Output file as .txt file to the analysis folder
output_path = os.path.join("analysis", "PyPoll_Results.txt")
with open(output_path, "w") as textfile:
    textfile.write(output_result)

