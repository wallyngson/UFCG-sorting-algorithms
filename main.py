import bubble
import selection
import insertion


array = [1, 3, 20, 18, 7, 50, 2]

print('Sorting using BubbleSort Algorithm:')
bubble.sort(array)

print('Sorting using SelectionSort Algorithm')
selection.sort(array)

print('Sorting using InsertionSort Algorithm')
insertion.sort(array)