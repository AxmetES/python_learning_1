# Use enumerate() and other skills to return a dictionary which has the
# values of the list as keys and the index as the value. You may assume
# that a value will only appear once
# in the given list.


def d_list(d_list):
    list_tuples = [(item, number) for number, item in enumerate(d_list)]
    return dict(list_tuples)


print(d_list(['a', 'b', 'c']))

# {'a': 0, 'b': 1, 'c': 2}

# [(0, 'a'), (1, 'b'), (2, 'c')]

# lst = ['a', 'b', 'c']
# list_tup = []
# for number, item in enumerate(lst):
#     list_tup.append((item, number))
# print(list_tup)



# correct version )))
# def d_list(L):
    # return {key: value for value, key in enumerate(L)}
