"""
Building a Trie in Python
Before we start let us reiterate the key components of a Trie or Prefix Tree.
A trie is a tree-like data structure that stores a dynamic set of strings.
Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.

Before we move into the autocomplete function we need to create a working trie for storing strings. We will create two classes:

A Trie class that contains the root node (empty string)
A TrieNode class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.

Finding Suffixes

Now that we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature.
To do that, we need to implement a new function on the TrieNode object that will return all complete word suffixes that exist below it in the trie.
For example, if our Trie contains the words ["fun", "function", "factory"] and we ask for suffixes from the f node,
we would expect to receive ["un", "unction", "actory"] back from node.suffixes().

(Hint: recurse down the trie, collecting suffixes as you go.)
"""


## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.root

        for char in word:
            current_node.insert(char)
            current_node = current_node.children[char]
        current_node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current_node = self.root

        for char in prefix:
            if char not in current_node.children:
                return None
            current_node = current_node.children[char]
        return current_node


## Represents a single node in the Trie

class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}

    def insert(self, char):
        ## Add a child node in this Trie
        if char not in self.children:
            self.children[char] = TrieNode()
            #self.children.value = char

    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for
        ## all complete words below this point
        all_suffixes = []
        try:
            child_nodes = self.children
        except:
            print('there is no child')
            return None

        for child_node in child_nodes.items():
            if child_node[1].is_word == True: # It is a word
                all_suffixes.append(suffix + child_node[0]) # append the current suffix to the list of suffixes

                if child_node[1].children is not None:
                    all_suffixes += child_node[1].suffixes(suffix+ child_node[0])
            else:
                all_suffixes += child_node[1].suffixes(suffix + child_node[0])

        return all_suffixes

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

test_case = ('ant', ['hology','agonist','onym'])
def test_function(test_case):
    suffixes = MyTrie.find(test_case[0]).suffixes()
    solution = test_case[1]
    if sorted(suffixes) == sorted(solution):
        print(suffixes)
        print("Pass")
    else:
        print("Fail")

test_case_1 = ['ant', ['hology','agonist','onym']]
test_function(test_case_1)

test_case_2 = ['a', ['nt', 'nthology','ntagonist','ntonym']]
test_function(test_case_2)

test_case_3 = ['f', ['un','unction','actory']]
test_function(test_case_3)

test_case_4 = ['t', ['rie','rigger','rigonometry', 'ripod']]
test_function(test_case_4)
