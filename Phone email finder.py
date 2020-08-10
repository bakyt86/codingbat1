import re
import pyperclip

telregex = re.compile(r'\d{3}-\d{3}-\d{4}')
emailregex = re.compile(r'''(
    [a-zA-Z0-9-_+-.]+   # name email
    @                   # sobachka
    [a-zA-Z_-]+         # domain
    \.                  # point
    [a-z]{2,4}          # com,re,org
    )''', re.VERBOSE)
text = pyperclip.paste()
result = []

for i in telregex.findall(text):
    result.append(i)
for i in emailregex.findall(text):
    result.append(i)

text = '\n'.join(result)
if len(text) != 0:
    pyperclip.copy(text)
else:
    print('Not found')



