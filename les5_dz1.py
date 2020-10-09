my_f = open('test.txt', 'w')
l = input('Введите текст \n')
while l:
    my_f.writelines(l)
    l = input('Введите текст \n')
    if not l:
        break

my_f.close()
my_f = open('test.txt', 'r')
cont = my_f.readlines()
print(cont)
my_f.close()
