wh=True
my_list = [7, 5, 3, 3, 2]
def permutation(a, value):
    max_value = max(a)
    if value > max_value:
        a.insert(0,value)
    elif value in a:
        a.insert(a.index(value),value)
    else:
        a.append(value)
        

while wh==True:
    permutation(my_list, int(input("введите число")))
    print(my_list)
