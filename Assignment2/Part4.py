"""
Andrew Murdoch
100707816

This program uses a min-Heap and Huffman's algorithm to determine the prefix codes of ASCII characters in a text file.
To run program use second argument as txt file directory. e.g. python Part4.py txt
"""
import heapq
import sys
from collections import Counter
from bitarray import bitarray


# Returns list of prefix codes
def createHuffmanTree(frequencyDict):
    heap = [[fq, [symbol, ""]] for symbol, fq in frequencyDict.items()]  # Create list of nodes with appropriate frequency and symbol
    heapq.heapify(heap)  # Transform list into min-heap

    while len(heap) > 1:
        left = heapq.heappop(heap)  # Get min node (root)
        right = heapq.heappop(heap)  # Get min node after first pop (root)

        for pair in left[1:]:  # Add zero to all the left note
            pair[1] += '0'
        for pair in right[1:]:  # Add zero to all the right note
            pair[1] += '1'
        heapq.heappush(heap, [left[0] + right[0]] + left[1:] + right[1:])  # Insert new node into heap

    huffmanList = left[1:] + right[1:]  # Create list with characters and their corresponding prefix codes

    return huffmanList


# Returns encoded string
def encode(string, ls):
    dct = {a[0]: bitarray(str(a[1])) for a in ls}
    encodedText = bitarray()
    encodedText.encode(dct, string)
    return encodedText


# Get data from file
file_name = sys.argv[1]
f = open(file_name, "r")
data = f.read()
f.close()
# Count each frequency of chars
freq = Counter(data)

huffList = createHuffmanTree(freq)  # Get prefix codes for each char
encodedString = encode(data, huffList)  # Get encoded string using prefix codes

print("Original String from ASCII file:", data)
for i in huffList:
    print("Char:", "'" + i[0] + "'", "freq:", freq[i[0]], "code:", i[1])
print("Encoded String:", encodedString)
print("Old length:", len(data))
print("New length", encodedString.length())
