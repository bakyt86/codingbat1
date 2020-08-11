import string
import random

while True:
    y = int(input('Enter a lengs '))

    x = string.ascii_letters + string.digits + string.punctuation
    print(''.join(random.sample(x,y)))





