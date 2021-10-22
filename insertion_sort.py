def insertion_sort(arr):
    for index in range(1, len(arr)):
        i = index
        while not(i-1 < 0) and (arr[i] < arr[i-1]):
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i -= 1

    return arr
