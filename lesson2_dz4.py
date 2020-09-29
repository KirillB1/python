        
a_input=input("введите строку слов с пробелами")

lst=a_input.split()

lst_len=len(lst)

counter=int(0)

n=1

while lst_len!=counter:
    


    print_lst=lst[counter]
    print("№",n," : ",print_lst[:10])
    counter=counter+1
    n=n+1
