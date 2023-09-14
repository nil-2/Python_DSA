def solution(arr):
    for i in range(0,n):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i] # swapping 
    print(sorted(arr))
if __name__=='__main__':
    arr = [1,0,-2,4,-5,6,-3,8]
    n = len(arr)
    solution(arr)