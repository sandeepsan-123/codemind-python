n=int(input())
l=list(map(int,input().split()))
k=sum(l)
c=k//n
s=0
for i in range(n):
    if l[i]>=c:
        s+=1
print(s)