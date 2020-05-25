# Assign a variable for the file to load and the path.
# file_to_load = 'Resources/election_results.csv'
# Open the election results and read the file
# with open(file_to_load) as election_data:
# print(election_data)

# Add our dependencies.
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the open() function with the "w" mode we will write data to the file.
# open(file_to_save, "w")
# Write some data to the file.
# outfile.write("Hello World")
# Close the file
# outfile.close()

# Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    # txt_file.write("Counties in the Election\n------------------\n")
    # Write three counties to the file.
    # txt_file.write("Arapahoe\nDenver\nJefferson")
#1. Initialize a total vote counter
total_votes = 0
# Create a list of candidates
candidate_options =[]
# Declare an empty dictionary of votes for each candidate
candidate_votes = {}

# Open the election results and read the file.
with open(file_to_load) as election_data:
# Print the file object.
# print(election_data)

# To do: read and analyze the data here. 
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Print each row in the CSV file.
    # for row in file_reader:
    #   print(row)
    # Read and print the header row.
    headers = next(file_reader)
        # print(headers)
    for row in file_reader:
        #2. Add to the total vote count.
        total_votes += 1
        # Print candidate name from each row
        candidate_name = row[2]
        # Add candidate name to the candidate list
        
        #if the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            # Add that nme to the list of candidates
            candidate_options.append(candidate_name)
            # Begin to track that candidate's vote count
            candidate_votes[candidate_name] = 0
            # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
        
        
#3. Print the total votes.
print(total_votes)
# Print the candidate list
print(candidate_options)
# Print candidate vote dictionary
print(candidate_votes)

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.

# Declare Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
for candidate in candidate_votes:
    # Retrieve vote count of a candidate
    votes = candidate_votes[candidate]
    # Calculate the % of votes
    vote_percentage = int(votes) / int(total_votes) * 100
    #  To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.
    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.        
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true then set winning_count = votes and winning_percent =
        # vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        # And, set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate
    #  To do: print out the winning candidate, vote count and percentage to
    #  terminal.
    # Print the candidate name and % of their votes    
    # To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.
    print(f"{candidate}: received {vote_percentage:.2f}% of the total votes.")
    print(f"{candidate}: {vote_percentage:.2f}% ({votes:,})\n")
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.2f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)



