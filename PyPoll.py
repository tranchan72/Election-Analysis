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
    print(headers)

