"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

# Creating a dictionary to store each phone number as a key, and their phone duration as value
my_dict = {}

# Creating a variable to track the highest phone duration
max_duration = 0

#Creating a variable to track the highest used phone's number
max_d_pn = None

# Creating a for loop to go though all the call records
for record in calls:
    pn1 = record[0]
    pn2 = record[1]

    call_duration = int(record[3])

    if pn1 in my_dict.keys():
        my_dict[pn1] += call_duration
    else:
        my_dict[pn1] = call_duration

    if pn2 in my_dict.keys():
        my_dict[pn2] += call_duration
    else:
        my_dict[pn2] = call_duration

    pn1_d = my_dict[pn1]
    pn2_d = my_dict[pn2]

    if pn2_d >= pn1_d:
        if max_duration < pn2_d:
            max_duration = pn2_d
            max_d_pn = pn2
    else:
        if max_duration < pn1_d:
            max_duration = pn1_d
            max_d_pn = pn1


print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(max_d_pn,max_duration))

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

