def sort(array):
    arr = array
    
    for i in range(len(arr)):
        min = i

        # walking around the list to find the 
        # element smaller than the current. 
        for j in range(i + 1, len(arr)):
            if (arr[j] < array[i]):
                min = j

        _swap(arr, min, i)
    
    print(arr)

# change the positions of two elements.
def _swap(arr, i, j):
    arr[j], arr[i] = arr[i], arr[j]
    