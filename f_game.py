doska = {'ustu_sol':'', 'ustu_orto':'', 'ustu_on':'',
         'orto_sol':'', 'orto_orto':'', 'orto_on':'',
         'pas_sol':'', 'pas_orto':'', 'pas_on':''}

def doska_tart():
    print(doska['ustu_sol'] + ' | ' + doska['ustu_orto'] + ' | ' + doska['ustu_on'])
    print('********')
    print(doska['orto_sol'] + ' | ' + doska['orto_orto'] + ' | ' + doska['orto_on'])
    print('********')
    print(doska['pas_sol'] + ' | ' + doska['pas_orto'] + ' | ' + doska['pas_on'])

doska_tart()

for i in range(9):
    x = input('x твой ход ')
    doska[x] = 'X'
    y = input('0 твой ход ')
    doska[y] = '0'
    doska_tart()
    
