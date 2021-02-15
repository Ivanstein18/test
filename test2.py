s=0
q=0
while True:
    a=int(input())
    s+=a
    q+=a**2
    if s==0:
        break
print(q)