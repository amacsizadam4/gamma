import random

def the_biggest(a,b,c):
    if a>=b:
        m=a
    else:
        m=b
    if m<=c:
        m=c
    return m

def the_smallest(a,b,c):
    if a<=b:
        m=a
    else:
        m=b
    if m>=c:
        m=c
    return m

a=random.randint(1,1000)
b=random.randint(1,1000)
c=random.randint(1,1000)
print(the_smallest(a,b,c))