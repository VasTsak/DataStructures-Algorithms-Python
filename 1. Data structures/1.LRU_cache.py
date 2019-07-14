# -*- coding: utf-8 -*-
"""
Least Recently Used Cache

We have briefly discussed caching as part of a practice problem while studying hash maps.

The lookup operation (i.e., get()) and put() / set() is supposed to be fast for a cache memory.

While doing the get() operation, if the entry is found in the cache, it is known as a cache hit. If, however, the entry is not found, it is known as a cache miss.

When designing a cache, we also place an upper bound on the size of the cache. If the cache is full and we want to add a new entry to the cache, we use some criteria to remove an element. After removing an element, we use the put() operation to insert the new element. The remove operation should also be fast.

For our first problem, the goal will be to design a data structure known as a Least Recently Used (LRU) cache. An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit. For the current problem, consider both get and set operations as an use operation.

Your job is to use an appropriate data structure(s) to implement the cache.

* In case of a cache hit, your get() operation should return the appropriate value.
* In case of a cache miss, your get() should return -1.
* While putting an element in the cache, your put() / set() operation must insert the element. If the cache is full, you must write code that removes the least recently used entry first and then insert the element.

All operations must take O(1) time.

For the current problem, you can consider the size of cache = 5.


@author: vasileios.tsakalos
"""
class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def set_key(self, key):
        new_node = Node(key)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.size = 1
        else:
            new_node.next = self.head
            self.head = new_node  # assign the new node as head
            while new_node.next:
                if key == new_node.next.key:
                    new_node.next = new_node.next.next
                    return
                new_node = new_node.next
            self.size += 1 # it increases the size only if it is a new key

    def get_key(self, key):

        if self.head is None:
            return None

        if self.head.key == key:
            return self.head.key

        node = self.head
        while node.next:
            if key == node.next.key:
                key =  node.next.key
                node.next = node.next.next
                break
            node = node.next
        new_node = Node(key)
        new_node.next = self.head
        self.head = new_node
        return self.head.key

    def delete_tail(self):
        node = self.head
        while node:
            if node.next is None:
                self.tail = node
            node = node.next
        tail = self.tail.key
        self.tail = None
        self.size -= 1
        return tail

l1 = LinkedList()
l1.set_key(1)
l1.set_key(2)
l1.set_key(3)

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.HashTable = dict()
        self.storage = LinkedList()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        try:
            return self.HashTable[self.storage.get_key(key)]
        except:
            return -1

    def set(self, key, value):
        # I set the value to the key first in case the key is already present in the hash table
        if key not in self.HashTable:
            self.storage.set_key(key)
        self.HashTable[key] = value
        if self.storage.size > self.capacity:
            del self.HashTable[self.storage.delete_tail()]
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.


our_cache = LRU_Cache(5)

# Test Case 1
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(3)       # return -1

print(our_cache.get(1))       # prints 1
print(our_cache.get(2))       # prints 2
print(our_cache.get(3))       # prints -1

# Test Case 2
# capacity at two
our_cache = LRU_Cache(2)

# fill out cache
our_cache.set(1, 'one')  # older
our_cache.set(2, 'two')  # newer

# executed a get, this means item 1 is *more* recently used than item 2.
print(our_cache.get(1))#one

# add a new item. this should remove item 2 because it is less recently used.
our_cache.set(3, 'three')

# item 1 should still be present
print(our_cache.get(1)) #one

# Test Case 3
our_cache = LRU_Cache(3)

our_cache.set(1, 1)
our_cache.get(1)       # returns 1

our_cache.set(2, 2)
our_cache.get(2)       # returns 2

our_cache.set(2, 3)
our_cache.get(2)       # returns 3

our_cache.set(1, 2)
our_cache.get(1)       # returns 2

our_cache.set(3, 4)
our_cache.set(4, 5)
our_cache.get(1)       # returns -1


print(our_cache.get(1))  # prints 2
print(our_cache.get(2))  # prints -1
print(our_cache.get(3))  # prints 4
print(our_cache.get(4))  # prints 5
