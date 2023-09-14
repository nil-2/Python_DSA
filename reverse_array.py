def solution(arr):
    print('Reversed Array :')
    n = len(arr)
    left = 0
    right = n-1
    
    while left<right:
        arr[left],arr[right] = arr[right],arr[left]
        left+=1
        right-=1
    print(arr)

if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8]
    print('original array :')
    print(arr)
    solution(arr)