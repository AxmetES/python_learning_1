# Use zip() and a list comprehension to return a list of the
# same length where each value is the two strings from
# L1 and L2 concatenated together with connector between
# them. Look at the example output below:


def concatenate(l1, l2, connector):
    list_zip = list(zip(l1, l2))
    list_join = [connector.join(i) for i in list_zip]
    return list_join


print(concatenate(['A', 'B'], ['a', 'b'], '-'))

# ['A-a', 'B-b'] output
