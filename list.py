b=['2',3,'4']
a=list(b)
print('the',a)
for item in a:
    print(item,end=' ')
del a[0]
print(a)
a.sort()#mutile will wrong
print(a)