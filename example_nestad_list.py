import random

list_result = []
while True:
    user = input('Y/N : ')
    if user == 'y':
        coin = random.randint(0, 1)
        if coin == 0:
            coin_pic = 'head'
        else:
            coin_pic = 'tail'
        list_result.append(coin_pic)
        print(coin_pic)
    else:
        break
print(list_result)
