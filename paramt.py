import __name__
def func(a,b=50,c=100):
    """This is a test.
    
    the fuc(a,b=50,c=100) print a,b,c."""
    print('a=',a,'b=',b,'c=',c)
    return
print(func.__doc__)
func(1)
func(1,2,3)
func(c=10,a=2)
help(func)

