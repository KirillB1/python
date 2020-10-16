with open('les5_dz3_file.txt', 'r') as file_les5_dz3:
    sa = []
    po = []
    my_list = file_les5_dz3.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
           po.append(i[0])
        sa.append(i[1])
print(f'Меньше 20.000 {po}, ср. оклад {sum(map(int, sa)) / len(sa)}')
