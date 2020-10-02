def my_func(a , b, c):
    if a >= b and b >= c:
        return a + b
    elif a > b and a < c:
        return a + c
    else:
        return b + c

print(my_func(int(input("введите первое число: ")), int(input("введите второе число ")), int(input("введите третье число "))))
