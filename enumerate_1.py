# Use enumerate() and other skills from above to return the count
# of the number of items in the list whose value equals its index.


def count_match_index(L):
    list_count = [iter for num, iter in enumerate(L) if iter == num]
    print(list_count)
    return len(list_count)


print(count_match_index([0, 2, 2, 1, 5, 5, 6, 10]))

# 4

# correct version
# def count_match_index(L):
#     return len([num for count, num in enumerate(L) if num == count])