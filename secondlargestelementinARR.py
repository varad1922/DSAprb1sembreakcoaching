# Given an array of integers nums, return the second-largest element in the array. If the second-largest element does not exist, return -1.
nums=int(input())
arr=list(map(int, input().split()))
largest= arr[0]
second= -1
for i in range(1, nums):
    if arr[i] > largest:
        second=largest
        largest=arr[i]
    elif arr[i]!= largest and (second== -1 or arr[i]> second):
        second=arr[i]
print(second)