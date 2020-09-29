
tup=[]
wh=True

while wh==True:
    n=+1 #номер продукта в кортеже
    product_name=input("введите название товара")
    key_product_name="название товара"

    the_price_of_the_product=int(input("введите цену товара"))
    key_the_price_of_the_product="цена продукта"

    quantity_of_goods=int(input("введите кол-во товара"))
    key_quantity_of_goods="кол-во товара"

    unit=input("введите еденицу измерения")
    key_unit="единица измерения"

    # упаковка кортежа в список
    tup.append((n, {key_product_name:product_name,key_the_price_of_the_product:the_price_of_the_product,key_quantity_of_goods:quantity_of_goods,key_unit:unit}),)
    print(tup)

    # сортировка по названию
    lst_name=[]
    lst_n=[]
    dict_couple={}
    the_price_of_the_product={}
    the_price_of_the_product_dict={}
    quantity_of_goods_dict={}
    unit_dict={}

    
    lst_n2=[]
    dict_i_tup2={}

    
    lst_n3=[]
    dict_i_tup3={}

    
    lst_n4=[]
    dict_i_tup4={}
    
    
    for i in tup:
        key_name="название товара"
        i_tup=i[1]
        dict_i_tup=i_tup[key_name]
        lst_n.append(dict_i_tup)
        dict_couple[key_name]=lst_n
        print(dict_couple)

    for i in tup:
        key_name="цена продукта"
        i_tup=i[1]
        dict_i_tup2=i_tup[key_name]
        lst_n2.append(dict_i_tup2)
        the_price_of_the_product_dict[key_name]=lst_n2
        print(the_price_of_the_product_dict)

    for i in tup:
        key_name="кол-во товара"
        i_tup=i[1]
        dict_i_tup3=i_tup[key_name]
        lst_n3.append(dict_i_tup3)
        quantity_of_goods_dict[key_name]=lst_n3
        print(quantity_of_goods_dict)

    for i in tup:
        key_name="единица измерения"
        i_tup=i[1]
        dict_i_tup4=i_tup[key_name]
        lst_n4.append(dict_i_tup4)
        unit_dict[key_name]=lst_n4
        print(unit_dict)
    
