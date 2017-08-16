import re

pattern1 = '^The'
m = re.search(pattern1, 'The end')  #匹配
if m is not None:
    print(m.group() )    #完整匹配
else:
    print(0)

pattern2 = '^The'
m = re.search(pattern2, 'end.The')  #不作为起始
if m is not None:
    print(m.group() )    #完整匹配
else:
    print(0)

pattern3 = r'\bthe'
m = re.search(pattern3, 'bite the dog')  #在边界
if m is not None:
    print(m.group() )    #完整匹配
else:
    print(0)

pattern4 = r'\bthe'
m = re.search(pattern4, 'bitethe dog')  #有边界
if m is not None:
    print(m.group() )    #完整匹配
else:
    print(0)

pattern5 = r'\Bthe'
m = re.search(pattern5, 'bitethe dog')  #没有边界
if m is not None:
    print(m.group() )    #完整匹配
else:
    print(0)

#能匹配到显示字符串，匹配不到显示0

    
