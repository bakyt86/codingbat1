Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============================ RESTART: F:/Питон/q1.py ===========================
12
>>> spam = [12, 34, 3, 1, 'Hello']

>>> spam[1]
34
>>> spam[2]
3
>>> spam[5]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    spam[5]
IndexError: list index out of range
>>> x = [[23, 4, 56], ['Hello',34]]
>>> x[0]
[23, 4, 56]
>>> x[0][0]
23
>>> x[1][0]
'Hello'
>>> spam[-1]
'Hello'
>>> spam[4]
'Hello'
>>> spam[-2]
1
>>> spam[0:-1]
[12, 34, 3, 1]
>>> spam[0:-2]
[12, 34, 3]
>>> spam[:4]
[12, 34, 3, 1]
>>> spam[2:]
[3, 1, 'Hello']
>>> spam[:]
[12, 34, 3, 1, 'Hello']
>>> len[spam]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    len[spam]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> len(spam)
5
>>> len(x)
2
>>> len(x[0])
3
>>> len(x[1])
2
>>> 