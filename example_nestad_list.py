import random

list_result = []
while True:
    user = input('do you want flip a coin ? Y/N : ')
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
count_tails = [x for x in list_result if x == 'tail']
count_heads = [x for x in list_result if x == 'head']

print(list_result)

print(f' tails  = {len(count_tails)}')
print(f' heads  = {len(count_heads)}')
