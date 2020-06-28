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

# Part A

# Creating a set to store the phone numbers's area code
area_codes_list = set()

# Creating a variable to store the count of calls made to banglore (080)
banglore_count = 0

# Creating a variable to store the count of calls made from banglore (080)
total_count = 0

# Creating a for loop to verify all the call records
for record in calls:
    if record[0][:5] == "(080)":
        total_count += 1
        pn = record[1]
        if(pn[0] == "("):
            if pn[:5] == "(080)":
                banglore_count += 1
            area_code = pn.split(")")[0]
            area_codes_list.add(area_code[1:])
        elif (pn[0] in ['7','8','9']):
            area_code = pn[:4]
            area_codes_list.add(area_code)
        else:
            area_codes_list.add("140")

# Sorting the set to get the numbers in lexicographic order
area_codes_list = sorted(area_codes_list)

print("The numbers called by people in Bangalore have codes:")
# Printing each area code in a seperate line
print("\n".join(area_codes_list))


# Part B

percentage = ((banglore_count/total_count)*100)

# Rounding the percentage value to 2 decimals
percentage = percentage.__round__(2)

print(str(percentage) + " percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
