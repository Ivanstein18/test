a=[]
c=input()
a=a.append(c)
a = [int(i) for i in a.split()]
b=0
q=0
for i in a:
    b+=i
    q+=i**2
    if b==0:
        break
print(q)