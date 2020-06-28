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


# Creating a Set object in order to find the unique phone numbers in the records,
# as a set does not allow duplicate values

rec_set = set()

#records is a variable to store the values of calls an texts
#type of record is a 'list'

records = texts + calls

# Creating a for loop to go through all the text and call records
for record in records:
    rec_set.add(record[0])
    rec_set.add(record[1])

# Printing all count of unique telephone numbers

print("There are " + str(len(rec_set)) + " different telephone numbers in the records.")
  

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
