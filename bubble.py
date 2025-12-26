# Given an array of integers called nums,sort the array in non-decreasing order using the bubble sort algorithm and return the sorted array.

nums=list(map(int,input().split()))
n=len(nums)
for i in range(n):
    for j in range(0, n-i-1):
        if nums[j]>nums[j+1]:
            nums[j], nums[j+1]=nums[j+1],nums[j]
print("Sorted Array:", *nums)