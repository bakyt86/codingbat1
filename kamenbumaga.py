from random import randrange

print('''Казан, кайчы, кагаз ойуну.
ойундун шарты:
    1 - Казан
    2 - Кайчы
    3 - Кагаз
''')

    
user = int(input('Cанды жаз\n'))
print(user)
if user == 1:
    print('Сиздин тандоонуз - Казан')
elif user == 2:
    print('Сиздин тандоонуз - Кайчы')
elif user == 3:
    print('Сиздин тандоонуз - Кагаз')
else:
    print('Сиз туура эмес санды жаздыныз!!!')

comp = randrange(3)+1
if comp == 1:
    print('Компьютердин тандоосу - Казан')
elif comp == 2:
    print('Компьютердин тандоосу - Кайчы')
elif comp == 3:
    print('Компьютердин тандоосу - Кагаз')Ы
    
if comp == user:
    print('Достук. Жениш бирдей')
elif comp == 1 and user == 2 or comp == 2 and user == 3 or comp == 3 and user == 1:
    print('Компьютер женди УРАА')
elif comp == 2 and user == 1 or comp == 3 and user == 2 or comp == 1 and user == 3:
    print('Сиз жендиниз УРАА')
    
