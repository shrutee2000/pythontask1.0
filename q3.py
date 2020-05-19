l1=[]
l2=[]
l3=[]
s=int(input("enter a no:"))
for i in range(s):
    n=int(input("enter a no"))
    l1.append(n)
for j in range(len(l1)):
    if l1[j]%2==0:
        l2.append(l1[j])
    else:
        l3.append(l1[j])

print("even list:")
print(l2)
print("odd list: ")
print(l3)