# Add our dependencies.
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis_challenge.txt")

total_votes = 0
# Create a list of candidates
candidate_options =[]
# Declare an empty dictionary of votes for each candidate
candidate_votes = {}
# Declare a list of counties
counties_options = []
# Declare an empty dictionary of counties
county_votes = {}
# Declare Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
winning_county = ""
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read and print the header row: # print(headers)
    headers = next(file_reader)    
    for row in file_reader:
        # Add to the total vote count.
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
        county_name = row[1]
        if county_name not in counties_options:
            counties_options.append(county_name)
            county_votes[county_name] = 0
        county_votes[county_name] += 1   

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
# Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    txt_file.write("County Votes:\n")
    for county in county_votes:
        votes = county_votes[county]
        vote_percentage = float(votes) / float(total_votes) * 100
        county_results = (f"{county}: {vote_percentage:.2f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(county_results)
        txt_file.write(county_results)
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_county = county
    county_largest_vote = (
        f"\n-------------------------\n"
        f"Largest county turn out: {winning_county}\n"
        f"-------------------------\n")
    txt_file.write(county_largest_vote,)
    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate in candidate_votes:
        # Retrieve vote count and %
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate}: {vote_percentage:.2f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.        
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.2f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    
    
    county_vote_percentage = (
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.2f}%\n"
    )
    # Save to text file
    txt_file.write(winning_candidate_summary)
