def rem(arr):
    if not arr:
        return []
    res=[arr[0]]
    for i in range(1,len(arr)):
        if arr[i]!=arr[i-1]:
           res.append(arr[i])
    return res

arr=[1,2,3,3,4,4,5]
un=rem(arr)
print(un)
    
