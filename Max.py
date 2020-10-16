#Max.py
a=int(input('第一个数：'))
b=int(input('第二个数：'))
c=int(input('第三个数：'))
if a>b and a>c:
    max=a
elif b>a and b>c:
    max=b
else:
    max=c
print(max)
