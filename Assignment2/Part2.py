"""
Andrew Murdoch
100707816

This program performs radix sort on unsorted array using counting sort on each digit.
"""
import numpy as np


# Get value of current digit
def getDigit(num, digit):
    working = num / 10 ** (digit - 1)
    return working % 10


def countingSort(arr, place):
    n = len(arr)

    output = [0] * n  # Initialize the sorted array with 0 as placeholder

    count = [0] * 10  # Initialize the count array with 0

    # Store the count of occurrences in count array
    for i in range(0, n):
        count[int(getDigit(arr[i], place))] += 1
    # Transform count array so that it contains the position of each element
    for i in range(1, 10):
        count[i] += count[i - 1]
    # Build output array
    for i in range(n - 1, -1, -1):
        output[count[int(getDigit(arr[i], place))] - 1] = arr[i]
        count[int(getDigit(arr[i], place))] -= 1
    #
    for i in range(0, len(arr)):
        arr[i] = output[i]


def radixSort(arr):
    maxNumber = max(arr)  # Get largest integer

    d = len(str(maxNumber))  # Get length of largest integer
    # Loop over each digit from least to most significant
    for place in range(1, d + 1):
        countingSort(arr, place)


# Driver code

array = [530519, 913652, 223528, 832955, 8769, 511593, 992345, 489746, 733572, 552452]
array1 = np.random.randint(0, 1000000, 10)  # Random array of 10 integers ranging from 1 (inclusive) to 1,000,000 (exclusive)

print("Unsorted array: ", array)
radixSort(array)
print("Sorted array: ", array, "\n ------------------------------")

print("Unsorted array: ", array1)
radixSort(array1)
print("Sorted array: ", array1)
