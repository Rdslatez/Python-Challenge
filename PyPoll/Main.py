import os
import csv
#Makes a path to read in the data as needed
voting_path = os.path.join( "PyPoll\Resources", "election_data.csv")
#Opens the files to read
with open(voting_path, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    #Pre declares some lists and variables to ensure they remain the proper data types
    temp = ''
    #Candidates and votes and variable lists so that the code is not brute forced and can be used for any number of canditates
    candidates = ['']
    votes = []
    total = 0
    #Begin reading the file row by row
    for row in csvreader:
        check = False
        length = len(candidates)
        #Temp is used as a go between the two lists of row and lists of candidates
        temp = row[2]       
        #This is a safety net to find the very first row, regardless of what it is
        if candidates[0] == '':  
            #candidates already has a 0 key since it is declared as an empty part of the list  
            candidates[0] = temp
            #votes contains no values, so it must be appended
            votes.append(1)
            #adds to the total number of votes.
            total =  total + 1
            check = True
        else:
            for i in range(length):
                #this loop checks if the row contains an already known candidate. If not, it will add a new candidate and vote list to store their votes specifically.
                if row[2] == candidates[i]:
                    #A known candidate is found, so the votes for it are added to.
                    votes[i] = votes[i] + 1
                    total =  total + 1
                    #check is used to ensure that when it's True, we will not duplicate the vote, and show that we found the candidate already
                    check = True
                    break
        #Candidate is not found, much like the safety net, this adds a new candidate and place in votes to store their votes.
        if check == False:
            candidates.append(temp)
            votes.append(1)
            total =  total + 1
            check = True
    #Opens up a path to a new file if it exists
    if os.path.exists(r'PyPoll\Analysis\analysis.csv'):
        #finds the path, and sets f as what we'll use to write to the file.
        f = open(os.path.join("PyPoll\Analysis", "analysis.csv"), 'w')
    #opens a new file since one was not found.
    else:
        #Creates a new file in this path to write to
        f = open(r'PyPoll\Analysis\analysis.csv', 'x')
    #writing to file and terminal/formatting
    f.write("Election results: \n")
    print("Election results: ")
    f.write(("--------------\n"))
    print("--------------")
    f.write("Total votes: ")
    f.write(str(total))
    f.write("\n")
    print("Total votes: ", total)
    f.write("--------------\n")
    print("--------------")
    countvote = 0
    #goes through the number of candidates/vote storage places there are
    for i in range(length):  
        #Checks to see who has the largest number of votes.
        if votes[i] > countvote:
              countvote = votes[i]
              winner = candidates[i]
        f.write(str(candidates[i]))
        f.write(": %")
        f.write(str("%.3f" % ((votes[i]/total) * 100)))
        f.write("  (")
        f.write(str(votes[i]))
        f.write(")\n")
        print(candidates[i], ": %", "%.3f" % ((votes[i]/total) * 100),  "  (", votes[i], ")")
    f.write("---------------\n")
    print("---------------")
    f.write("Winner: ")
    f.write(str(winner))
    print("Winner: ", winner )
   
    
    
