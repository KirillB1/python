

def division(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("деление на ноль")
c=int(input("введите делимое"))
d=int(input("введите делитель"))
print(division(c,d))
