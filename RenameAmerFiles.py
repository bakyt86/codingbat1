import os
import shutil
import re

obrazest = re.compile(r'''^(.*?)
    ((0|1)?\d)-
    ((0|1|2|3)?\d)-
    ((19|20)\d\d)
    (.*?)$
''',re.VERBOSE)
for i in os.listdir(r'C:\Users\Пользователь\Desktop\AmerFiles'):
    mo = obrazest.search(i)
    if mo == None:
        continue
    beforeMonth = mo.group(1)
    month = mo.group(2)
    day = mo.group(4)
    year = mo.group(6)
    afterYear = mo.group(8)

    evroFile = beforeMonth + day + '-' + month + '-' + year + afterYear
    shutil.move(r'C:\Users\Пользователь\Desktop\AmerFiles\%s'%(i),r'C:\Users\Пользователь\Desktop\AmerFiles\%s'%(evroFile))
    
