# Given two integer arrays nums1 and nums2. Both arrays are sorted in non-decreasing order.
nums1=list(map(int,input().split()))
nums2=list(map(int,input().split()))
i=0
j=0
merged=[]
while i < len(nums1) and j < len(nums2):
    if nums1[i] <=nums2[j]:
        merged.append(nums1[i])
        i+=1
    else:
        merged.append(nums2[j])
        j+=1
while i< len(nums1):
    merged.append(nums1[i])
    i+=1
while j< len(nums2):
    merged.append(nums2[j])
    j+=1
print("Merged Array:", *merged)
