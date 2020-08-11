import re
import pyperclip
# 0778 74 37 78, (0778)987363, +996779-87-98-98
kgregex = re.compile(r'\(?0?\d{3}\)? \d{2} \d{2} \d{2}|\+996 \d{3} \d{2} \d{2} \d{2}')
text = pyperclip.paste()
result = []

for i in kgregex.findall(text):
    result.append(i)

text = '\n'.join(result)
if len(text) != 0:
    pyperclip.copy(text)
else:
    print('Not found')

