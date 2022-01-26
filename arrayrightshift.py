arr=[1,2,3,4,5]

def arrayrightshiftbyone(arr,n):
    temp=arr[n-1]
    for i in range(n-1,-1,-1):
        arr[i]=arr[i-1]
    arr[0]=temp

def arrayrightshift(arr,d,n):
    for i in range(d):
        arrayrightshiftbyone(arr,n)

arrayrightshift(arr,3,len(arr))
print(arr)

