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

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""

def main():

    max_time_spent = 0
    phone_numbers = {}
    for call in calls:
        if call[0] in  phone_numbers:
            phone_numbers[call[0]] += int(call[3])
        else:
            phone_numbers[call[0]] = int(call[3])
        if call[1] in phone_numbers:
            phone_numbers[call[1]] += int(call[3])
        else:
            phone_numbers[call[1]] = int(call[3])

    for number, time_spent in phone_numbers.items():
        if time_spent > max_time_spent:
            max_time_spent = int(time_spent)
            max_number = number
    print(max_number,"spent the longest time,", max_time_spent," seconds, on the phone during September 2016.")

if __name__ == '__main__':
    main()
