def sort(array):
    arr = array

    for i in range(len(arr)):
        aux = arr[i]
        pos = i

        # while the previous element is large than current element
        # and the current position is than 0, position change.
        while (pos > 0 and arr[pos - 1] > aux):
            _swap(arr, pos, pos - 1)

            position -= 1
    
    print(arr)
    
# change the positions of two elements.
def _swap(arr, i, j):
    arr[j], arr[i] = arr[i], arr[j]