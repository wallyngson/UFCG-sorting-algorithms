def sort(array):

    # Optimized Bubble Sort.

    arr = array
    swapped = True

    # while there are exchanges the algorithm
    # will keep running.
    while(swapped):
        swapped = False

        # walking one by one looking for the largest
        # and exchanging the positions.
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                _swap(arr, i, i + 1)
                swapped = True
   
    print(array)
    
# change the positions of two elements.
def _swap(arr, i, j):
    arr[j], arr[i] = arr[i], arr[j]
    

