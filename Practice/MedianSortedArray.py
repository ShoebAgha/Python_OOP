def findMedianSortedArrays(nums1, nums2):
    i,j=0,0
    merged=[]
    while i < len(nums1) and j < len(nums2):
        if nums1[i]<nums2[j]:
            merged.append(nums1[i])
            i+=1
        else:
            merged.append(nums2[j])
            j+=1
    if i==len(nums1):
        merged.extend(nums2[j:])
    else:
        merged.extend(nums1[i:])
    
    if len(merged)%2==1:
        median = int(len(merged)/2)
        return merged[median]
    else:
        median = int(len(merged)/2)-1
        return (merged[median]+merged[median+1])/2

print(findMedianSortedArrays([1,3,5,7],[2,4,8,9]))


