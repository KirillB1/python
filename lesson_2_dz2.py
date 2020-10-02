wh=True
l = []
while wh==True:
    
    l.append(input("введите значение переменной"))
    j = 0
    for i in range(int(len(l)/2)):
        l[j], l[j+1] = l[j+1], l[j]
        j += 2

    print(l)
