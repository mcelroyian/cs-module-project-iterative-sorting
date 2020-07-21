def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    start = 0
    end = len(arr) -1
    
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        if target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1  # not found
