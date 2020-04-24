def findMedianSortedArrays(nums1, nums2):
    l = len(nums1) + len(nums2)
    if l % 2:
        s = int(l / 2) + 1
    else:
        s = int(l / 2)
    list_merge = []
    i = m = n = 0
    if nums1 == [] or nums2 == []:
        return max(nums1, nums2)[s-1] if 2*s != l else float(max(nums1, nums2)[s-1] + max(nums1, nums2)[s])/2
    while(i <= s):
        if m <= len(nums1) - 1 and n <= len(nums2) - 1:
            if nums1[m] <= nums2[n]:
                list_merge.append(nums1[m])
                m = m + 1
            else:
                list_merge.append(nums2[n])
                n = n + 1 
        elif m >= len(nums1):
            list_merge.append(nums2[n])
            n = n + 1
        else:
            list_merge.append(nums1[m])
            m = m + 1
        i = i + 1
    if s == int(l / 2):
        return float(list_merge[s] + list_merge[s-1]) / 2
    else:
        return list_merge[s-1]

findMedianSortedArrays([3, 4], [])