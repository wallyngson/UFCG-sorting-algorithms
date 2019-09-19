def sort(array):
    arr = array
    
    for i in range(len(arr)):
        min = i
        for j in range(i + 1, len(arr)):
            if (arr[j] < array[i]):
                min = j

        _swap(arr, min, i)
    
    print(arr)

def _swap(arr, i, j):
    arr[j], arr[i] = arr[i], arr[j]
    