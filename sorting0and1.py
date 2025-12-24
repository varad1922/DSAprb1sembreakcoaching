# Problem Statement: Given an array of length N consisting of only 0s and 1s in random order. Modify the array to segregate 0s on the left and 1s on the right side of the array.
arr=list(map(int, input().split()))
n=len(arr)
for i in range(n):
    for j in range(0,n-i-1):
        if arr[j]>arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(*arr)