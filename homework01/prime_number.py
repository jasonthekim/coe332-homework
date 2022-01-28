for i in range(3,100):
    prime = True
    for j in range(3,i):
        if (i % j == 0):
            prime = False
    if prime:
        print(i)


