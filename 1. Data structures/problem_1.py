"""
Least Recently Used Cache

The lookup operation (i.e., get()) and put() / set() is supposed to be fast for a cache memory.

While doing the get() operation, if the entry is found in the cache, it is known as a cache hit. If, however, the entry is not found, it is known as a cache miss.

When designing a cache, we also place an upper bound on the size of the cache. If the cache is full and we want to add a new entry to the cache, we use some criteria to remove an element. After removing an element, we use the put() operation to insert the new element. The remove operation should also be fast.

For our first problem, the goal will be to design a data structure known as a Least Recently Used (LRU) cache. An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit. For the current problem, consider both get and set operations as an use operation.

Your job is to use an appropriate data structure(s) to implement the cache.

In case of a cache hit, your get() operation should return the appropriate value.
In case of a cache miss, your get() should return -1.
While putting an element in the cache, your put() / set() operation must insert the element. If the cache is full, you must write code that removes the least recently used entry first and then insert the element.
All operations must take O(1) time.

For the current problem, you can consider the size of cache = 5.

Here is some boiler plate code and some example test cases to get you started on this problem:
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    def enqueue(self, value):
        new_node = Node(value)
        if self.num_elements == 0:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
        self.num_elements += 1

    def dequeue(self):
        if self.num_elements == 0:
            return None
        value = self.head.value
        self.num_elements -= 1
        return value

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.HashTable = dict()
        self.storage = Queue()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        try:
            return self.HashTable[key]
        except:
            return -1

    def set(self, key, value):
        # I set the value to the key first in case the key is already present in the hash table
        self.HashTable[key] = value
        if self.storage.size() > self.capacity:
            del self.HashTable[self.storage.dequeue()]
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.

our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(3)       # return -1

print(our_cache.get(1))       # prints 1
print(our_cache.get(2))       # prints 2
print(our_cache.get(3))       # prints -1
