n=int(input())
f=0
for i in range(1,n):
    if i*i==n:
        f=1
        break
if f==1:
    print("perfect")
else:
    print("not a perfect")