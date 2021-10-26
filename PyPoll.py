# The data we need to retrieve.
# 1. Total number of votes cast
# 2. Complete list of candidates who received votes
# 3. Percentage of votes each candidate won
# 4. Total number of votes each candidate won
# 5. Winner of the election based on popular vote

import csv
import os
# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join('analysis', 'election_analysis.txt')

# 1. Initialize a total vote counter
total_votes = 0

# Declare Candidate options and candidate votes
candidate_options = []
candidate_votes = {}

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)

    # Print each row in the CSV file
    for row in file_reader:
        
        # 2. Add to the total vote count
        total_votes += 1

        # Print candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            # Add candidate name to candidate list
            candidate_options.append(candidate_name)
            # Begin tracking candidate's vote count
            candidate_votes[candidate_name] = 0

         # Add vote to candidate's count
        candidate_votes[candidate_name] += 1

    # Determine percentage of votes for each candidate by looping through counts
    # Iterate through candidate list
    for candidate_name in candidate_votes:
        # Retrieve vote count of candidate
        votes = candidate_votes[candidate_name]
        # Calculate percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print the candidate name and percentage of votes
        print(f'{candidate_name}: received {vote_percentage:.1f}% of the vote')


# Print candidate vote dictionary
print(candidate_votes)


# Close the file
election_data.close()

# Using with statement, open file as a text file
with open(file_to_save, 'w') as txt_file:

    # Write three counties to the file
    txt_file.write('Counties in the Election\n---------------\nArapahoe\nDenver\nJefferson')
