def my_summ ():
    summ_res = 0
    e = False
    while e == False:
        number = input('Спецсимвол Q или q ,введите строку раздёлённую пробелом').split()

        summ = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                e = True
                break
            else:
                summ = summ + int(number[el])
            summ_res = summ_res+summ
        
        print(f'Текущая сумма{summ_res}')
    


my_summ()

