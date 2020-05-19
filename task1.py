def calc(a,b):
    def sum():
        s=a+b
        return s
    return sum()+5
c=int(input("enter no 1"))
d=int(input("enter no 2"))
result=calc(c,d)
print(f"addition={result}")