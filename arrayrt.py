arr=[10,20,30,40,50,60]

def arrayrotatebyone(arr,n):
    temp=arr[0]
    for i in range(n-1):
        arr[i]=arr[i+1]
    arr[n-1]=temp

def arrayrotate(arr,d,n):
    for i in range(d-1):
        arrayrotatebyone(arr,len(arr))


def printarray(arr,n):
    for i in range(n):
        print("%d"%arr[i],end="  ")

arrayrotatebyone(arr,len(arr))
arrayrotate(arr,4,len(arr))
printarray(arr,len(arr))