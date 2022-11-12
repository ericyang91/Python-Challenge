import os
import csv

election = os.path.join(r"C:/Users/ericj/Desktop/Challenges/Python-Challenge/PyPoll", "Resources", "election_data.csv")
results = open("C:/Users/ericj/Desktop/Challenges/Python-Challenge/PyPoll/Analysis/Analysis.txt", "w")

with open(election, 'r') as electioncsv:
    pypollreader = csv.reader(electioncsv, delimiter=',')
    total_vote = []
    candidate_list = []
    
    
    header = next(pypollreader)
    for row in pypollreader:
        
        total_vote.append(row[2])

        if row[2] not in candidate_list:
            candidate_list.append(row[2])

total_number_votes = int(len(total_vote))

print('Election Results:')
results.write('Election Results:\n')
print(f"The total number of votes was: {total_number_votes} votes")
results.write(f"The total number of votes was: {total_number_votes} votes\n")

vote_per_candidate = {}
winner = 0

for list in candidate_list:
    vote_per_candidate[list] = total_vote.count(list)
    if total_vote.count(list) > winner:
        winner = total_vote.count(list)
        winning_candidate = list
    
    print(f"Candidate {list} received {total_vote.count(list)} votes, which makes up {round(int(total_vote.count(list))/ total_number_votes * 100, 2)}% of the total votes.")
    results.write(f"Candidate {list} received {total_vote.count(list)} votes, which makes up {round(int(total_vote.count(list))/ total_number_votes * 100, 2)}% of the total votes.\n")
   
print(f"The winning candidate is {winning_candidate}. Congratulations!")
results.write(f"The winning candidate is {winning_candidate}. Congratulations!")