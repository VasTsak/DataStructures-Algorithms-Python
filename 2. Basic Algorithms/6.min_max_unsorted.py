"""
Max and Min in a Unsorted Array
In this problem, we will look for smallest and largest integer from a list of unsorted integers.
The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.

Bonus Challenge: Is it possible to find the max and min in a single traversal?
"""

def get_min_max(ints):

    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return None, None
    max = ints[0]
    min = ints[0]
# since we have initialized max and min with the first element
    for element in ints[1:]:
        if element < min:
            min = element
            continue # if it is smaller than the current min there is no chance of being bigger than the max
        if element > max:
            max = element
    return min, max

### Test cases

import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

l = [i for i in range(0, 10000)]  # a list containing 0 - 99999
random.shuffle(l)

print ("Pass" if ((0, 9999) == get_min_max(l)) else "Fail")

l = [i for i in []]  # a list containing nothing
random.shuffle(l)

print ("Pass" if ((None, None) == get_min_max(l)) else "Fail")

l = [i for i in [1]]  # a list containing nothing
random.shuffle(l)

print ("Pass" if ((1, 1) == get_min_max(l)) else "Fail")
