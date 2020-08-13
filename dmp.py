

import os

####os.makedir(r'C:\Users\Public\Desktop\as\as\as\as\as\as\as\as')
##a = ''
##for i in range(10):
##    a = a + r'\papka%s'%(i)
##os.makedirs(r'C:\Users\Public\Desktop' + a)    
##
##    
x = r'C:\Users\Public\Desktop' 

for i in range(5):
    os.makedirs(x + r'\hello%s'%(i))
    

for i in range(5):
    
    f = open(x+r'\hello%s\file.txt'%(i), 'w')
    f.write('Hello world')
    f.close()
