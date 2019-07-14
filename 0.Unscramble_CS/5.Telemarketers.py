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

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def main():
    unique_outgoing_calls = []
    unique_not_outgoing_calls = []
    potential_telemarketer = []

    for text in texts:
        unique_not_outgoing_calls.append(text[0])
        unique_not_outgoing_calls.append(text[1])
    for call in calls:
        unique_not_outgoing_calls.append(call[1])
        unique_outgoing_calls.append(call[0])

    for oc in unique_outgoing_calls:
        if oc not in unique_not_outgoing_calls:
            potential_telemarketer.append(oc)
    potential_telemarketer = list(set(potential_telemarketer))
    potential_telemarketer.sort()

    print("These numbers could be telemarketers: ")
    for pt in potential_telemarketer:
        print(pt)

if __name__ == '__main__':
    main()
