import pyperclip
import sys

a = {'Куба':'Куба кечиресин, азыр мен бош эмесмин. Кийинираак сага чалам',
     'Курманбек':'Курманбек азыр бош эмесмин, бошогондо чалам'}

x = sys.argv[1]
if x in a:
    pyperclip.copy(a[x])
    print('copied')
else:
    print('No found')

