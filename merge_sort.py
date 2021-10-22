def merge_sort(arr):
    if len(arr) == 1:
        return arr
    else:
        mid_index = len(arr) // 2
        right_half = merge_sort(list(arr[mid_index:]))
        left_half = merge_sort(list(arr[:mid_index]))

        return sort_lists(right_half, left_half)

