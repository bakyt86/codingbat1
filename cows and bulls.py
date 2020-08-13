import random
import string

##number = random.sample(string.digits,4)
##number = ''.join(number)
##print(number)

number = ''

for i in range(4):
    number += str(random.randint(0,9))
print(number)
for i in range(5):
    user = input('Enter a 4 digits ')
    cow = 0
    bull = 0
    for i in range(4):
        if user[i] == number[i]:
            cow += 1
        if user[i] in number and user[i]!= number[i]:
            bull += 1
    print('cow: ' + str(cow) + ' bull: ' + str(bull))        
    

    
