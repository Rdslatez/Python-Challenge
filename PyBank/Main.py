import os
import csv
#Makes a path to read in the data as needed
budget_path = os.path.join( "PyBank\Resources", "budget_data.csv")
#Begins reading the file. Rest of the code does not to be within this, but does not fail because of it.
with open(budget_path, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    #Declaring variables for the sake of future need. Some need to be declared as 0 and not as null
    header = next(csvreader)
    great = 0
    greatmonth = ''
    change = 0
    chatotal = 0
    low = 0
    lowmonth = ''
    temp = 0
    months = 0
    total = 0
    #Begins reading in the data
    for row in csvreader:
        #This is to calculate total loss/profits overall
        total += float(row[1])
        #Temp is for the change in profits/losses, and it will always start at 0 since it must be between months, not before data is collected.
        if temp == 0 :
            temp = float(row[1])
        else:
            #Since temp is saved as the row before, change can equal the current row, minus temp/the row previous and it's profit/loss
            change = float(row[1]) - temp
            #adds to the total change
            chatotal += change
            #changes temp back to the current row for the next iteration
            temp = float(row[1])
            #The following if's check to see if the current change is greater than what is currently known as the biggest increase of profit
            if change > great:
                great = change
                greatmonth = row[0]
            #Same as previous, but if the decreasing change is smaller/bigger negative than the known biggest decrease
            if change < low:
                low = change
                lowmonth = row[0]
        #adds to the month count. Needs to be after the header since it doesn't count as a month
        months += 1
    #Calculates the average change between loss/profits
    chatotal = chatotal/(months-1)
    #Writes all as needed for the assignment, along with some spacing.
    print("Financial Analysis: ")
    print("---------------------------------")
    print("Total months: ", months)
    print("Total: $", total)
    
    print("Average Change: $", "%.2f" % chatotal)
    print("Greatest increase in profits: ", greatmonth , "($", "%.0f" % great, ")")
    print("Greatest decrease in profits: ", lowmonth , "($", "%.0f" % low, ")")
    #Checks if there is a file that already exists in resources to write to
    if os.path.exists(r'PyBank\Analysis\analysis.csv'):
        #finds the path, and sets f as what we'll use to write to the file.
        f = open(os.path.join("PyBank\Analysis", "analysis.csv"), 'w')
    else:
        #Creates a new file in this path to write to
        f = open(r'PyBank\Analysis\analysis.csv', 'x')
    #Same as printing to the terminal, but is writing to the file.
    f.write("Financial Analysis: \n")
    f.write ("---------------------------------\n")
    f.write("Total months: ")
    #Writing can't take multiple variables/inputs like print can, so they are done seperately
    f.write(str(months))
    f.write("\n")
    f.write("Total: $")
    f.write(str(total))
    f.write("\n") 
    f.write("Average Change: $")
    f.write(str("%.2f" % chatotal))
    f.write("\n")
    f.write("Greatest increase in profits: ")
    f.write(str(greatmonth))
    f.write("($")
    f.write(str("%.0f" % great))
    f.write(")\n")
    f.write("Greatest decrease in profits: ")
    f.write(lowmonth)
    f.write("($")
    f.write(str("%.0f" %low))
    f.write(")\n")
    f.close
            
    

