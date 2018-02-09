num=23
flag=True
while flag:
    guess=int(input('input the num'))
    if num==guess:
        flag=False
        print('right')
    elif num>guess:
        print("bigger than it")
    else:
        print("litter than it")
else:
    print('loop over')
print("over")
