my_list = [1, 2, 3, 4, 5]

gencomp = (item for item in my_list if item > 3)

gencomp_iter = iter(gencomp)
for item in gencomp_iter:
    print(item)

print(next(gencomp_iter))
