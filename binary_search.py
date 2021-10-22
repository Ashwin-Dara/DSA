def binary_search(arr, target):
    arr.sort()
    low = 0
    high = len(arr)

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return True

        if target > arr[mid]:
            low = mid + 1

        if target < arr[mid]:
            high = mid - 1

    return False
