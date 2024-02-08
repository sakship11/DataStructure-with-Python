#Selection sort
def selectionsort(arr):
    for i in range(len(arr)):
        min_idx=i
        for j in range(i+1,len(arr)):
            if arr[min_idx]>arr[j]:
                min_idx=j
        arr[i],arr[min_idx]=arr[min_idx],arr[i]

arr=[64,34,12,69,54]
print("Array before sorting")
print(arr)
selectionsort(arr)
print("Sorted Array")
print(arr)
