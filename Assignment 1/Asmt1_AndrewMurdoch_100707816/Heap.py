"""
#Andrew Murdoch
#100707816

This program uses the class MaxHeap to create and manipulate a max heap.
"""
import math


class MaxHeap:
    # initialize max heap
    def __init__(self, array):
        self.Heap = array
        self.size = len(self.Heap)
        self.buildMaxHeap()  # Build max heap on initialization

    def parent(self, pos):
        return pos // 2

    def leftChild(self, pos):
        return 2 * pos

    def rightChild(self, pos):
        return (2 * pos) + 1

    # Builds max heap
    def buildMaxHeap(self):
        for i in range(self.size, -1, -1):
            self.maxHeapify(self.Heap, i, self.size)  # call max heapify on all sub trees

    # max heapify function
    def maxHeapify(self, array, pos, n):
        left_child = self.leftChild(pos)  # get left and right child
        right_child = self.rightChild(pos)
        largest = pos
        if left_child < n and array[left_child] > array[largest]:  # if left child is largest
            largest = left_child
        if right_child < n and array[right_child] > array[largest]:  # if right child is largest
            largest = right_child
        if largest != pos:  # if largest is not parent swap largest and parent
            temp = array[pos]
            array[pos] = array[largest]
            array[largest] = temp
            self.maxHeapify(array, largest, n)  # call max heapify on new parent

    # insert value into heap
    def insert(self, x):
        array = self.Heap
        length = self.size + 1
        array.insert(length, x)
        i = len(array) - 1
        while array[i] > array[int(math.floor(i / 2))] and i > 0:
            temp = array[i]
            array[i] = array[int(math.floor(i / 2))]
            array[int(math.floor(i / 2))] = temp
            i = int(math.floor(i / 2))

    # print heap in array format
    def printAsArray(self):
        print(self.Heap)

    # print heap in tree format
    def printAsTree(self, root):
        if self.size > 0:
            print(self.createTreePrint(self.Heap, root, 0))

    # create tree for printing
    def createTreePrint(self, array, root, depth):
        left_child = 2 * root + 1
        right_child = 2 * root + 2
        tree = ""
        if right_child < len(array):
            tree += self.createTreePrint(array, right_child, depth + 1)  # print right child recursively

        tree += "\n" + (depth * "\t") + str(array[root])

        if left_child < len(array):
            tree += self.createTreePrint(array, left_child, depth + 1)  # print left child recursively

        return tree

    # get max value in heap
    def max(self):
        return self.Heap[0]

    # extract max in heap
    def extractMax(self):
        if self.size < 1:
            print("heap underflow")

        returnMax = self.max()
        self.Heap[0] = self.Heap[self.size - 1]  # replace max with last element in heap
        self.Heap.pop()  # pop last value after storing in first index
        self.size = self.size - 1
        self.maxHeapify(self.Heap, 0, self.size)  # call heapify on root node
        return returnMax

    # sort heap
    def heapSort(self, array):
        self.buildMaxHeap()  # rebuild max heap if needed
        for i in range(self.size, 0, -1):
            array[i], array[0] = array[0], array[i]  # swap root with current index in loop
            self.maxHeapify(array, 0, i)  # call max heapify on sub tree


# Driver code
print('The maxHeap\n')
arr = [2, 1, 4, 10, 8, 7, 3, 9, 14, 16]
print("Array is: ", arr)
print("Creating max heap: ")
maxHeap = MaxHeap(arr)
maxHeap.printAsArray()
maxHeap.printAsTree(0)
print("Largest value in heap (max): ", maxHeap.max())
print("Extract the max value: ", maxHeap.extractMax())
maxHeap.printAsTree(0)
b = 12
print("Insert ", b, "into heap: ")
maxHeap.insert(b)
maxHeap.printAsTree(0)
print("Before Sorting: ")
maxHeap.printAsArray()
print("Sorted heap using heap sort: ")
maxHeap.heapSort(maxHeap.Heap)
maxHeap.printAsArray()
maxHeap.printAsTree(0)
