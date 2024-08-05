def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
    
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key

elements = [1, 4, 2, 8, 23]

insertion_sort(elements)

print("Sorted elements:", elements)
