import re

s = 'This and that'
v = re.findall(r'(th\w+) and (th\w+)', s, re.I)
h = re.finditer(r'(th\w+) and (th\w+)', s, re.I)

a = re.sub('X', 'Mr.Smith', 'attn: X\n\nDear X, \n')

DATA = ('Mountain View, CA 94040',
        'Sonnyvale, CA',
        'Los Altos, 94023',
        'Cupertino 95014',
        'Palo Alto CA')
for datum in DATA:
    print(re.split(', |(?= (?:\d{5}|[A-Z]{2})) ', datum))
