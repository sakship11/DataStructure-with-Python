#Linear Search
def search(arr,n,x):
    for i in range(0,n):
        if arr[i]==x:
            return True
arr=[1,2,3,4,5,6,7,8,9]
x=9
n=len(arr)
result=search(arr,n,x)
if result==True:
    print("Element Present")
else:
    print("Element not Present")
