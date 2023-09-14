def solution(arr):
    sum1 = 0
    sum2 = 0
    print('sum of even elements :')
    for i in range(0,n):
        if arr[i]%2==0:
            sum1 = sum1+arr[i]
    print(sum1)
    
    print('sum of odd elements : ')
    for i in range(0,n):
        if arr[i]%2!=0:
            sum2 = sum2+arr[i]
    print(sum2)
if __name__=='__main__':
    arr =[1,2,4,7,9,13,5,14]
    n = len(arr)
    solution(arr)