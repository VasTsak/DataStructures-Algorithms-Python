"""
Search in a Rotated Sorted Array
You are given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target value to search. If found in the array return its index, otherwise return -1.

You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).

Example:

Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4
"""
def rotated_array_search(input_list, number, start_index, end_index):

    if len(input_list) == 0:
        return -1
    if start_index > end_index:
        return -1

    mid_index = (start_index + end_index) // 2
    if input_list[mid_index] == number:
        return mid_index

    # in case the part of list we keep is sorted:
    if input_list[start_index] <= input_list[mid_index]:
        # it is easy for us because we do just a binary search
        if number >= input_list[start_index] and number <= input_list[mid_index]:
            return rotated_array_search(input_list, number, start_index, mid_index - 1)
        return rotated_array_search(input_list, number, mid_index + 1, end_index)

    # in case the part of list we keep is not sorted, it means that the other part is sorted
    if number >= input_list[mid_index] and number <= input_list[end_index]:
        start_index = mid_index + 1
        return rotated_array_search(input_list, number, mid_index + 1, end_index)
    return rotated_array_search(input_list, number, start_index, mid_index - 1)

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number, 0, len(input_list) -1):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[], None])
test_function([[], 1])
