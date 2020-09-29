list_a=[]
b_int=int(33)
c_str=str('test_str')
d_bool=bool(True)
e_list=list('a,b,c,d,e')
f_float=float(123.123)
d_tuple=(tuple('1,2,3,4,5'))
e_dict={1:"a",2:"b",3:"c",4:"d",5:"e"}

list_a.append(e_dict)
list_a.append(d_tuple)
list_a.append(b_int)
list_a.append(f_float)
list_a.append(e_list)
list_a.append(d_bool)
list_a.append(c_str)
list_a.append(b_int)
type_print=type(list_a)

quantity=len(list_a)
step=0

while quantity!=step:
    type_list_value=type(list_a[step])
    step_print=step+1
    value=list_a[step]
    print("элемент №",step_print,"___тип__",type_list_value,'содержание__:',value)
    step=step+1

