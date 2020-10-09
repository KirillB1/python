n=0
my_file = open('file_les5_dz2.txt', 'r')
content = my_file.read()
print(f'Содержимое файла: \n {content}')
my_file = open('file_les5_dz2.txt', 'r')
content = my_file.readlines()
print(f' Количество строк в файле - {len(content)}')
my_file = open('file_les5_dz2.txt', 'r')
content = my_file.readlines()

for i in range(len(content)):
    n=i
    print(f'Окличество символов {i + 1} - ой строки {len(content[i])}')
my_file = open('file_les5_dz2.txt', 'r')
content = my_file.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')
my_file.close()
