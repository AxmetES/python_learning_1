new_list = [34, 23, 1, 15, 4, 8, 10]


def bobble_sort(mylist):
    last_item = len(mylist) - 1
    for i in range(last_item):
        for j in range(last_item):
            if mylist[j] > mylist[j + 1]:
                mylist[j], mylist[j + 1] = mylist[j + 1], mylist[j]
    return mylist


print(bobble_sort(new_list))
