def kthlargestelement(arr):
    n = len(arr)
    print('kth largest element :')
    for i in range(0,n):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                temp = arr[i]
                arr[i]=arr[j]
                arr[j]=temp
    print(arr[n-k])
    
def kthsmallestelement(arr):
    n1 = len(arr)
    print('kth smallest element :')
    for m in range(0,n1):
        for l in range(m+1,n1):
            if arr[m]<arr[l]:
                temp = arr[m]
                arr[m]=arr[l]
                arr[l]=temp
    print(arr[n1-k])
if __name__=='__main__':
    arr = [1,0,2,25,7,9,15,100,89]
    k = int(input('enter kth term :'))
    kthlargestelement(arr)
    kthsmallestelement(arr)
    