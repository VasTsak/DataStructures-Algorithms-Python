import hashlib
import datetime

class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.next = None
      self.previous_hash = previous_hash
      self.hash = self.calc_hash(self.timestamp, self.data, self.previous_hash)

    def calc_hash(self, timestamp, data, previous_hash):

      sha = hashlib.sha256()

      hash_str = (str(timestamp) + str(data) + str(previous_hash)).encode('utf-8')

      sha.update(hash_str)

      return sha.hexdigest()

    def set_previous_hash(self, h):
        self.previous_hash = h

    def get_hash(self):
        return self.hash

block1 = Block(datetime.datetime.now(), [1, 2, 3], None)
block2 = Block(datetime.datetime.now(), [4, 5, 6], None)
block3 = Block(datetime.datetime.now(), [7, 8, 9], None)

def build_chain(old_node, new_node):
    old_node.next = new_node
    new_node.set_previous_hash(old_node.get_hash())
    return old_node, new_node

block1, block2 = build_chain(block1, block2)
block2, block3 = build_chain(block2, block3)

# Test case 1
print(block1.get_hash() == block1.next.previous_hash) # True

# Test case 2
print(block2.get_hash() == block1.next.next.previous_hash) # True

# Test case 3
print(block2.get_hash() == block2.next.previous_hash) # True

# Test case 4
print(block2.get_hash() == block3.previous_hash) # True

# Test case 5
print(block1.get_hash() == block3.previous_hash) # False
