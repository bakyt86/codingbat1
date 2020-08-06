while True:
    x = input('Enter word ')
    if x == '':
        break
    x = x.lower()
    if x[::-1] == x:
        print('Palindrome')
    else:
        print('Not palindrome')
