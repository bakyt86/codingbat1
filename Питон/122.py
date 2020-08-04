Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = [23, 4, 67, 09, 'Hello']
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> x = [23, 4, 67, 9, 'Hello']
>>> y = [87, 90, 5, 'Ok']
>>> x + y
[23, 4, 67, 9, 'Hello', 87, 90, 5, 'Ok']
>>> x*2
[23, 4, 67, 9, 'Hello', 23, 4, 67, 9, 'Hello']
>>> del x[4]
>>> x
[23, 4, 67, 9]
>>> 
========================================================================================================= RESTART: F:/Питон/1212.py ========================================================================================================
Enter cat name or press enter to exit Tom 
Enter cat name or press enter to exit Bars
Enter cat name or press enter to exit Pet
Enter cat name or press enter to exit 
Tom 
Bars
Pet
>>> 