import re

data = 0
string = type(data)
str = 'classs'

print(str)
v = re.search('class', str)
if v != None:
    m = v.group()
    print(m)
