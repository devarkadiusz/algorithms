#!/bin/python
import sys
def insertion_sort(array):
    for index in range(1, len(array)):
        value = array[index ]
        i = index - 1
        while i >= 0 and value < array[i]:
            array[i + 1] = array[i]
            i -= 1

        array[i + 1] = value
    return array

array = [int(x) for x in sys.argv[1:]]
print(" ".join([str(x) for x in insertion_sort(array)]))

