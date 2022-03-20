for i in range(7):
    for j in range(i+1):
        if j != i:
            print(j, end=',')
        else:
            print(j)