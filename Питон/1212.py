cats = []
while True:
    name = input('Enter cat name or press enter to exit ')
    if name == '':
        break
    cats = cats + [name]
for i in cats:
    print(i)
    
