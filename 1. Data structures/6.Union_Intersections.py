# -*- coding: utf-8 -*-
"""
Union and Intersection of Two Linked Lists

Your task for this problem is to fill out the union and intersection functions.
The union of two sets A and B is the set of elements which are in A, in B, or in both A and B.
The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both the sets A and B.

You will take in two linked lists and return a linked list that is composed of either the union or intersection, respectively.
Once you have completed the problem you will create your own test cases and perform your own run time analysis on the code.

"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def search(self, value):

        if self.head is None:
            return None

        node = self.head
        while node:
            if value == node.value:
                return node
            node = node.next

    def remove_dups(self, value):

        if self.head is None:
            return
        count = 0
        if self.head.value == value:
            count += 1

        node = self.head
        while node.next:
            if node.next.value == value:
                count += 1
                if count > 1:
                    node.next = node.next.next
                    return
            node = node.next

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    # Your Solution Here
    union_list = LinkedList()

    parse_l1 = llist_1.head

    if llist_1.head is None:
        return llist_2
    if llist_2.head is None:
        return llist_1

    while parse_l1:
        union_list.append(parse_l1.value)
        parse_l1 = parse_l1.next


    parse_l2 = llist_2.head

    while parse_l2:
        union_list.append(parse_l2.value)
        parse_l2 = parse_l2.next


    first = union_list.head

    while first is not None:
        union_list.remove_dups(first.value)
        first = first.next
    return union_list

def intersection(llist_1, llist_2):
    # Your Solution Here
    inter_list = LinkedList()

    if llist_1.head is None:
        return "The first linked list is empty"
    if llist_2.head is None:
        return "The second linked list is empty"
    head = llist_1.head

    while head.next:
        int_node = llist_2.search(head.value)
        if int_node:
            inter_list.append(int_node.value)
        head = head.next

    first = inter_list.head

    while first is not None:
        inter_list.remove_dups(first.value)
        first = first.next
    if inter_list.head is None:
        return "There are no common elements"
    return inter_list


if __name__ == "__main__":
    # Test case 1

    linked_list_1 = LinkedList()

    linked_list_2 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,21]
    element_2 = [6,32,4,9,6,1,11,21,1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print (union(linked_list_1,linked_list_2)) # 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 32 -> 9 -> 1 -> 11 -> 21 ->
    print (intersection(linked_list_1,linked_list_2)) # 4 -> 6 ->

    # Test case 2

    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,23]
    element_2 = [1,7,8,9,11,21,1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print (union(linked_list_3,linked_list_4)) # 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 ->
    print (intersection(linked_list_3,linked_list_4)) # There are no common elements

    # Test case 3

    linked_list_5 = LinkedList()
    linked_list_6 = LinkedList()

    element_1 = []
    element_2 = [6,7,8,9,10]

    for i in element_1:
        linked_list_5.append(i)

    for i in element_2:
        linked_list_6.append(i)

    print (union(linked_list_5,linked_list_6)) #  6 -> 7 -> 8 -> 9 -> 10
    print (intersection(linked_list_5,linked_list_6)) # The first linked list is empty


    # Test case 4

    linked_list_7 = LinkedList()
    linked_list_8 = LinkedList()

    element_1 = ''
    element_2 = [6,7,8,9,10]

    for i in element_1:
        linked_list_7.append(i)

    for i in element_2:
        linked_list_8.append(i)

    print (union(linked_list_7,linked_list_8)) # 6 -> 7 -> 8 -> 9 -> 10
    print (intersection(linked_list_7,linked_list_8)) # The first linked list is empty
