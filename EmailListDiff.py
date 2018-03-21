#Reads in csv file1 and searches entire csv file2 if it contains any member of
#file1 is in file2. File1 members that don't have a match are writtnn into an
#output file "diff.csv". Matching of the rows in each file is done using the
#email addresses
#First row of each file is assumed to be header and is skipped.

import csv
print(" \n")
print("FIRST LINE OF .csv FILE SKIPPED AS HEADER\n")

fn1 = input("Enter incremental csv filename1: ")
fname1 = open(fn1,"r")
next(fname1)                        # to skip header row
csv_fname1 = csv.reader(fname1)     # required for csv read

fn2 = input("Enter master csv filename2: ")
fname2 = open(fn2,"r")

wordlist =[]     # define an empty list
count = 0
with open('diff.csv', "w") as outfile:
    writer = csv.writer(outfile, lineterminator='\n')
        # required for csv write; lineterminator prevents extra line feeds
    for row in csv_fname1:         #iterate over each row element in fname1
        for word in row:
            if "@" in word:             #picks email id
                wordlist.clear()        #empty the list for row processing
                wordlist.append(word)   #convert to a single entry list
        found = 0
        fname2.seek(0)
        next(fname2)                    # to skip header row
        csv_fname2 = csv.reader(fname2)
        for line in csv_fname2:         #iterate over all rows of fname2
            if len(set(wordlist) & set(line)) == 0: # no match
                continue
            else:
                found= 1
                break
        if(not found):
            count += 1
            print(row)
            writer.writerow(row)
    print("\nTotal number of new email addresses = ",count)
