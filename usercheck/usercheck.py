import csv
import itertools

newresults = []
thefile = open('output.txt', 'w')

fileone = []
with open('existing.csv', newline='') as existing_file:
    for row in csv.reader(existing_file):
        fileone.append(row)
        
filetwo = []
with open('lastnametest.csv', newline='') as inputfile:
    for row in csv.reader(inputfile):
        filetwo.append(row)        
       
#currentUsers = list(itertools.chain(*fileone))
#searchUsers = list(itertools.chain(*filetwo))

#current_list = [name for name in currentUsers if name.strip()]
#search_list = [name for name in searchUsers if name.strip()]

current_list = [name for names in filetwo for name in names if name.strip()]
search_list = [name for names in fileone for name in names if name.strip()]


for i in current_list:
    for j in search_list:
        if i == j:
            newresults.append(i)
       

for item in newresults:
    thefile.write("%s\n" % item)
