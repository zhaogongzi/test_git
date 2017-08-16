import re

string = 'www.yahu123.com'
data = ('www.lili.net',
        'www.yahu.com',
        'www.baddu.edu',
        'baidu.com')
pattern = r'www.(\w+|\d+)(.com|.net|.edu)'

for datum in data:
    m = re.search(pattern, datum)
    if m != None:
        v = m.group()
        print(v)
