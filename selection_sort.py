def selection_sort(arr):
    n = len(arr)
    for i in range(0, n):
        minIndex = i
        for j in range(i, n):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]

    return arr
