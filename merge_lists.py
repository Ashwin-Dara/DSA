def merge_lists(arr1, arr2):
    sorted_arr = []
    for i in range(max(len(arr1), len(arr2))):
        # Cases to consider
        # When both values at the same indices are equal
        # When one of them longer than the other
        if i > (len(arr1) - 1):
            sorted_arr += [arr2[i]]
        elif i > (len(arr2) - 1):
            sorted_arr += [arr1[i]]
        elif arr1[i] > arr2[i]:
            sorted_arr += [arr2[i]] + [arr1[i]]
        else:
            sorted_arr += [arr1[i]] + [arr2[i]]

    return sorted_arr
