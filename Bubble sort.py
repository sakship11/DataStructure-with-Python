#Bubble sort
def bubblesort(arr):
    n=len(arr)
    for i in range(n):
        swapped=False
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if swapped==False:
            break
arr=[64,34,25,12,22,11,90]
print("Array before sort")
print(arr)
bubblesort(arr)
print("Sorted Array")
print(arr)
