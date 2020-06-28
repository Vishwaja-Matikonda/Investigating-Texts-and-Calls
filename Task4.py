"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""

import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

# Creating a counter to count the telemarketing calls
count = 0

# Creating a set ot store all phone numbers which have texted as well as received calls
my_set = set()

# Creating a for loop to go through all the text records
for record1,record2 in zip(texts,calls):
    my_set.add(record1[0])
    my_set.add(record1[1])
    my_set.add(record2[1])

# Creating a set to save possible tele marketing numbers
telemarketing_list = set()

# for loop to check if the dialing numbers are part of set or not
for record in calls:
    pn = record[0]
    if pn not in my_set:
        telemarketing_list.add(pn)

telemarketing_list = sorted(telemarketing_list)

print("These numbers could be telemarketers: ")
print("\n".join(telemarketing_list))

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order 
with no duplicates.
"""