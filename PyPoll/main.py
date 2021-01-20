# PyPoll

# Import modules
import os
import csv

# Define csv file path
poll_csv_path = os.path.join("Resources", "election_data.csv")

# Open and read csv with defined delimiter
with open(poll_csv_path) as poll_file:
    poll_csv = csv.reader(poll_file, delimiter=",")

    # Read first row as header
    header = next(poll_csv)

    # Define lists
    voter_ids = []
    candidates = []
    candidates_set = []
    poll_counts = []
    poll_pct = []
    results = []

    # Set variables equal to 0 at start
    total_votes = 0
    poll_loop = 0
    pct_loop = 0
    most_votes = 0
    results_loop = 0

    # Read each row of dataset csv and add to each assigned value
        # Assign column 0 to voter_id values and column 2 to candidate values
        # Add each row/vote from dataset to voter_ids list
        # Add each row/vote from dataset to candidates list
    for row in poll_csv:
        voter_id = row[0]
        candidate = row[2]
        voter_ids.append(voter_id)
        candidates.append(candidate)
    # Test
    # Length of candidates list is equal to length of voter_ids list (3,521,001)
    # print(len(candidates))

    # Calculate total number of votes cast
    total_votes = len(set(voter_ids))
    # Test
    # Length of candidates list is equal to length of voter_ids list (3,521,001)
    # print(total_votes)

    # Generate complete list of unique candidates who received votes (4)
    candidates_set = (sorted(set(candidates)))
    # Tests
    # print(candidates_set)
    # print(len(candidates_set))
    # print(candidates_set[0])
    # print(candidates_set[1])
    # print(candidates_set[2])
    # print(candidates_set[3])

    # Create integer variable for number of unique candidates to use in future loop (4)
    candidate_index = int(len(candidates_set))
    # print(candidate_index)
    
    # Count total number of votes each candidate won and add to poll_counts list
    # Need to calculate total votes per candidate first to use in calculation to find percentage of votes per candidate
    for poll_loop in range(candidate_index):
        poll_counts.append(candidates.count(candidates_set[poll_loop]))
    # Test
    # print(candidates_set)
    # print(poll_counts)

    # Calculate percentage of votes each candidate won and add to poll_pct list
    for pct_loop in range(candidate_index):
        poll_pct.append((poll_counts[pct_loop] / total_votes) * 100)
    # Test
    # print(poll_pct)

        # Find election winner based on highest popular vote
        # Conditional loop must be nested under pct_loop because we are using pct_loop as loop index
        if poll_counts[pct_loop] > most_votes:
            most_votes = poll_counts[pct_loop]
            winner = candidates_set[pct_loop]
    # Test
    # print(most_votes)
    # print(winner)

    # Loop to output vote counts and percentages using same index to ensure correlating results for each candidate
    for results_loop in range(candidate_index):
        results.append(f"{candidates_set[results_loop]}: {poll_pct[results_loop]:.3f}% ({poll_counts[results_loop]:,})")
    # print("\n".join(results))

    # Set results list equal to a variable to use loop for easier formatting
    results_summary = "\n".join(results)
    # print(results_summary)

# Print analysis results to terminal
analysis_results = (f"\
Election Results\n\
-------------------------\n\
Total Votes: {total_votes:,}\n\
-------------------------\n\
{results_summary}\n\
-------------------------\n\
Winner: {winner}\n\
-------------------------\n"
)

print(analysis_results)

# Export analysis results to text file
output_path = os.path.join("Analysis", "PyPoll_analysis_results.txt")
with open(output_path, "w") as PyPoll_txt:
    PyPoll_txt.write(analysis_results)
