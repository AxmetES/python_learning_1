# merge func
def merge(a, b):
    i = 0
    j = 0
    result = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result += a[i:] + b[j:]
    return result


# merge sort
def merge_sort(a):
    if len(a) > 1:
        return merge(merge_sort(a[:len(a) // 2]), merge_sort(a[len(a) // 2:]))
    else:
        return a


a = [8, 6, 4, 2, 9, 6, 5, 3, 2, 1, 1, 74, 85, 5, 1, 784, 222, 4, 4, 5, 8, 9, 10, 11, 25, 34, 97]
print(merge_sort(a))
