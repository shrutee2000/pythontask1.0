x=100
sample={'physics':88,'maths':75,'chemistry':72,'basic electrical':89}
for key,value in sample.items():
    if x>value:
        x=value
        y=key
print(y)