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
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""

def main():

    unique_number = []
    for text in texts:
        unique_number.append(text[0])
        unique_number.append(text[1])

    for call in calls:
        unique_number.append(call[0])
        unique_number.append(call[1])

    print("There are", len(set(unique_number)),"different telephone numbers in the records.")

if __name__ == "__main__":
    main()
