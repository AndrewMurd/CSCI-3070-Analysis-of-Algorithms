"""
#Andrew Murdoch
#100707816

This program applies binary search on a rotated array to find index of a key.
"""


# Finds last element of rotated array and performs standard binary search
def rotatedBinarySearch(arr, n, key):
    tail = findTail(arr, 0, n - 1)  # find index of last element of rotated array

    if tail == -1:  # if index of tail is -1 the array is not rotated
        return binarySearch(arr, 0, n - 1, key)

    if arr[tail] == key:  # check if tail is key
        return tail
    if arr[0] <= key:  # if array is rotated perform binary search around tail
        return binarySearch(arr, 0, tail - 1, key)
    return binarySearch(arr, tail + 1, n - 1, key)


# Function to get tail of rotated array
# [5, 9, 10, 1, 4] returns 2
def findTail(arr, low, high):
    # base cases
    if high < low:
        return -1
    if high == low:
        return low

    mid = int((low + high) / 2)

    if mid < high and arr[mid] > arr[mid + 1]:  # if element at mid is greater then next element you have found tail
        return mid
    if mid > low and arr[mid] < arr[mid - 1]:  # if element at mid is less then previous element you have found tail
        return mid - 1
    if arr[low] >= arr[mid]:  # continue searching for tail on either side of mid
        return findTail(arr, low, mid - 1)
    return findTail(arr, mid + 1, high)


# Binary Search function returns index of key
def binarySearch(arr, low, high, key):
    if high < low:
        return "None"

    mid = int((low + high) / 2)

    if key == arr[mid]:
        return mid
    if key > arr[mid]:
        return binarySearch(arr, (mid + 1), high, key)
    return binarySearch(arr, low, (mid - 1), key)


# Driver
arr2 = [5, 9, 10, 1, 4]
n = len(arr2)
key = 10
print("Index of the element is : ", rotatedBinarySearch(arr2, n, key))
