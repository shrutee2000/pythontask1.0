def myfunc(s1,s2,txt):
    s1=""
    s2=""

    for i in range(0,len(txt)):
        if txt[i].islower():
            s1=s1+txt[i]
        else:
            s2=s2+txt[i]
    return s1+s2

txt=input("enter a string")
myfunc(s1,s2,txt)