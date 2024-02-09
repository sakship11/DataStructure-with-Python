#Insertion sort
def insertionsort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
arr=[12,32,2,11,8,5]
print("Array before sorting")
print(arr)
insertionsort(arr)
print("Array after sorting")
print(arr)
        
