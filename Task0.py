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
    

# Record1 stores the first record of 'texts.csv'

record1 = texts[0]

# Prints the first record of texts

print("First record of texts, {} texts {} at time {}".format(record1[0],record1[1],record1[2]))

# Record2 stores the first record of 'calls.csv'

record2 = calls[0]

# Prints the Last record of calls

print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(record2[0],record2[1],record2[2],record2[3]))


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""