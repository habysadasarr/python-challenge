# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidates = []
num_votes = []

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            num_votes.append(1)
        else:
            index = candidates.index(candidate_name)
            num_votes[index] += 1

# Winning Candidate and Winning Count Tracker
winner = max(num_votes)
index = num_votes.index(winner)
winning_candidate = candidates[index]

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:
    # Print the total vote count (to terminal)
    print("Election Results")
    print("--------------------------")
    print(f"Total Votes: {str(total_votes)}")
    print("--------------------------")

    # Write the total vote count to the text file
    txt_file.write("Election Results\n")
    txt_file.write("--------------------------\n")
    txt_file.write(f"Total Votes: {str(total_votes)}\n")
    txt_file.write("--------------------------\n")

    # Loop through the candidates to determine vote percentages and identify the winner
    percent_votes = []
    for votes in num_votes:
        percentage = (votes / total_votes) * 100
        percentage = round(percentage, 3)
        percent_votes.append(f"{percentage:.3f}%")

    for i in range(len(candidates)):
        candidate_output = f"{candidates[i]}: {percent_votes[i]} ({num_votes[i]})"
        print(candidate_output)
        txt_file.write(candidate_output + "\n")

    # Generate and print the winning candidate summary
    print("--------------------------")
    print(f"Winner: {winning_candidate}")
    print("--------------------------")

    # Save the winning candidate summary to the text file
    txt_file.write("--------------------------\n")
    txt_file.write(f"Winner: {winning_candidate}\n")
    txt_file.write("--------------------------\n")