def solution(arr,n):
    new_arr = []
    for i in arr:
        if i not in new_arr:
            new_arr.append(i)
    print(sorted(new_arr))
if __name__=='__main__':
    arr = [1,0,1,1,0,2,5,9,8,7,2,9,8,13,5]
    n= len(arr)
    solution(arr,n)

