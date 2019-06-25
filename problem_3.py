import sys

class HuffmanNode(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
        self.root = None
    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_root(self, root):
        self.root = root

def create_tree(node, encoding=""):
    if type(node) == str:
        return {node: encoding}
    l, r = node.get_left(), node.get_right()
    d = dict()
    d.update(create_tree(l, encoding + "0"))
    d.update(create_tree(r, encoding + "1"))
    return d

def sort_freq(data):
    freq = dict()

    for s in data:
        if s in freq:
            freq[s] += 1
        else:
            freq[s] = 1

    sorted_frequencies = sorted(freq.items(), key=lambda kv: kv[1], reverse = True)
    return sorted_frequencies

def huffman_encoding (data):
    encoded_data = ""
    if len(data) == 0: # in case the input string is empty
        return encoded_data, None
    sorted_data = sort_freq(data)
    if len(sorted_data) == 1:
        node = sort_freq(data)[0][0]
        for i in range(sort_freq(data)[0][1]):
            encoded_data += '0'
        return encoded_data, node
    while len(sorted_data) > 1:
        left, left_frequency = sorted_data[-1]
        right, right_frequency = sorted_data[-2]
        sorted_data = sorted_data[:-2]
        node = HuffmanNode(left, right)
        sorted_data.append((node, left_frequency + right_frequency))
        # Re-sort the list
        sorted_data = sorted(sorted_data, key=lambda x: x[1], reverse=True)

    codes = create_tree(sorted_data[0][0])

    for ch in data :
        encoded_data += codes[ch]
    return encoded_data, sorted_data[0][0]

def huffman_decoding (encoded_data, tree) :
    decoded_output = ""
    if len(encoded_data) == 0: # in case the input string is empty
        return decoded_output
    if type(tree) == str:
        for i in encoded_data:
            decoded_output += tree
        return decoded_output
    p = tree
    for bit in encoded_data:
        if bit == '0':
            p = p.get_left()
        else:
            p = p.get_right()

        if type(p) == str :
            decoded_output += p
            p = tree

    return decoded_output

if __name__ == "__main__":
    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2)))) # The size of the encoded data is: 36
    print ("The content of the encoded data is: {}\n".format(encoded_data)) # The content of the encoded data is: 1110100100010111000110101101100111111110111100010001011001110000101101

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data))) # 69
    print ("The content of the decoded data is: {}\n".format(decoded_data)) # The content of the decoded data is: The bird is the word

    empty_sentence = ""

    print ("The content of the data is: {}\n".format(empty_sentence)) # The content of the data is:

    encoded_data, tree = huffman_encoding(empty_sentence)

    print ("The content of the encoded data is: {}\n".format(encoded_data)) # The content of the encoded data is:

    decoded_data = huffman_decoding(encoded_data, tree) # The content of the data is:

    print ("The content of the decoded data is: {}\n".format(decoded_data)) # The content of the decoded data is:

    complex_great_sentence = "This is 1 cömplex sentence"

    print ("The size of the data is: {}\n".format(sys.getsizeof(complex_great_sentence)))
    print ("The content of the data is: {}\n".format(complex_great_sentence))

    encoded_data, tree = huffman_encoding(complex_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2)))) # The size of the encoded data is: 40
    print ("The content of the encoded data is: {}\n".format(encoded_data)) # The content of the encoded data is: 0100010111101011001101011000101000110010001100001001110010101111010001110111111110010111111100101

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data))) # The size of the decoded data is: 99
    print ("The content of the decoded data is: {}\n".format(decoded_data)) # The size of the decoded data is: 99

    lesser_great_sentence = "AAAAAAAA"

    print ("The size of the data is: {}\n".format(sys.getsizeof(lesser_great_sentence)))
    print ("The content of the data is: {}\n".format(lesser_great_sentence))

    encoded_data, tree = huffman_encoding(lesser_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2)))) # The size of the encoded data is: 24
    print ("The content of the encoded data is: {}\n".format(encoded_data)) # The content of the encoded data is: 00000000

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data))) # The size of the decoded data is: 57
    print ("The content of the decoded data is: {}\n".format(decoded_data)) # The content of the decoded data is: AAAAAAAA
