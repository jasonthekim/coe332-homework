x = [1, 3, 4, 6, 5, 6, 7, 8, 9, 10]

def even_or_odd(array):
    for i in x:
        if i % 2 == 0:
            print(f'{i} is even.')
        else:
            print(f'{i} is odd.')

y = even_or_odd(x)
print(y)


