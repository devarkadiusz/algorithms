#!/bin/python
import sys
def bubble_sort(array):
    i = j = 0
    while i < len(array):
        while j < len(array) - 1 - i:
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
            j += 1
        i += 1
        j = 0
    return array
array = [int(x) for x in sys.argv[1:]]
print(" ".join(map(str, bubble_sort(array))))

