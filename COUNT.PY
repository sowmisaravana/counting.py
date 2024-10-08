arr=[1,7,0,4,3,1,0,5,6,2,0,0,7,5,0,0]
n=len(arr)
k=max(arr)
count=[0]*(k+1)
b=[-1]*n
for i in range(n):
    count[arr[i]]=count[arr[i]]+1
for i in range(1,k+1):
    count[i]=count[i-1]+count[i]
for i in range(n-1,-1,-1):
    count[arr[i]]=count[arr[i]]-1
    b[count[arr[i]]]=arr[i]
print(b)