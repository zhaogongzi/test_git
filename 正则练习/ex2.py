import re

string = 'Smith White, S'

v = re.split(' |,', string)
print(v)
