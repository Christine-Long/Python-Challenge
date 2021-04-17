import os
import csv

# You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:
election_csv = os.path.join("C:/Users/Christine Long/Python-Challenge/PyPoll/Resources/election_data.csv")

totalvotes = 0
candidates = []
numbervote = []
percentages = []

# The total number of votes cast
with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)

    for row in csvreader:
        totalvotes += 1

        name = row[2]
# A complete list of candidates who received votes
        if name not in candidates:
            candidates.append(name) 

# The total number of votes each candidate won
            numbervote.append(1)
        else:
            candidateindex = candidates.index(name) 
            numbervote[candidateindex] += 1

# The percentage of votes each candidate won
    for votes in numbervote:
        percentage = round((votes/totalvotes)*100,3)
        percentages.append(percentage)

# The winner of the election based on popular vote.
    maxvote = max(numbervote)
    index = numbervote.index(maxvote)
    winner = candidates[index]

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.
print(f'''
Election Results
--------------------------
Total Votes: {totalvotes}
--------------------------
{candidates[0]}: {percentages[0]}% ({numbervote[0]})
{candidates[1]}: {percentages[1]}% ({numbervote[1]})
{candidates[2]}: {percentages[2]}% ({numbervote[2]})
{candidates[3]}: {percentages[3]}% ({numbervote[3]})
--------------------------
Winner: {winner}
--------------------------
''')

output_path = os.path.join("C:/Users/Christine Long/Python-Challenge/PyPoll/Poll_text.txt")

with open(output_path, 'w', newline = '') as textfile:
    textfile.write(f'''
Election Results
--------------------------
Total Votes: {totalvotes}
--------------------------
{candidates[0]}: {percentages[0]}% ({numbervote[0]})
{candidates[1]}: {percentages[1]}% ({numbervote[1]})
{candidates[2]}: {percentages[2]}% ({numbervote[2]})
{candidates[3]}: {percentages[3]}% ({numbervote[3]})
--------------------------
Winner: {winner}
--------------------------
''')