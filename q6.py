def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

print("1-add")
print("2-subtract")
print("3-multiply")
print("4-divide")
print("enter choice")
c=int(input("choice="))
if c in [1,2,3,4]:
    a=int(input("enter no1"))
    b=int(input("enter no2"))
    if c==1:
        print(add(a,b))
    elif c==2:
        print(sub(a,b))
    elif c==3:
        print(multiply(a,b))
    elif c==4:
        print(divide(a,b))
else:
    print("enter valid choice no")
