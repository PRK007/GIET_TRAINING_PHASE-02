text='the sun rises in the east '
v=['sun','in','east','doctor','day']

l=list(text.split())
s=set()
for i in l:
    if i not in v:
        s.add(i)

print(s)        

