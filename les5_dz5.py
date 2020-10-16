def summ():
    try:
        with open('les5_dz5_file.txt', 'w+') as file_o:
            line = input('Введите цифры через пробел \n')
            file_o.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')
summ()
