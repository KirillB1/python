surname = 'Surname'
name = 'Name'
year = '2222'
city = 'City_town'
e_mail = 'mail@mail.com'
telephone = '9-999-999-99-99'

def personal_data(name, surname, year, city, e_mail, telephone):
     return ' '.join([name, surname, year, city, e_mail, telephone])
    

print(personal_data(surname = 'Surname', name = 'Name', year = '2222', city = 'City_town', e_mail = 'mail@mail.com', telephone = '9-999-999-99-99')) 

