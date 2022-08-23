# -*- coding: utf-8 -*
nums = [5, 2, 6, 1, 23, 7, -12, 12, -243, 0]

# Bubble Sort
def bubble_sort(nums):
    n = len(nums)
    if n<2:
        return nums
    for _ in range(n-1):
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
    return nums

print(bubble_sort(nums))

# Insertion Sort
def insertion_sort(nums):
    n = len(nums)
    if n < 2:
        return nums
    for i in range(n):
        num = nums.pop(i)
        j = i-1
        while num <= nums[j] and j >= 0:
            j -= 1
        nums.insert(j+1, num)
    
    return nums

print(insertion_sort(nums))

# Merge Sort
# 先将数组分隔开，再两两merge到一起
def merge(nums1, nums2):
    nums = []
    i,j = 0,0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums[j]:
            nums.append(nums1[i])
            i += 1
        else:
            nums.append(nums2[j])
            j += 1
    # 一定有一个数组还没有遍历完
    nums1_tail, nums2_tail = nums1[i:], nums2[j:]
    return nums+nums1_tail+nums2_tail

def merge_sort(nums):
    n = len(nums)
    if n < 2:
        return nums
    mid = n//2
    left, right = nums[:mid], nums[mid:]
    left_sorted, right_sorted = merge_sort(left), merge_sort(right)
    
    return merge(left_sorted, right_sorted)

print(merge_sort(nums))

# Quick Sort
# 每一步去最后一个数字为阈值，将小于阈值的放在左侧，大于阈值的放在右侧，再迭代对左右数组进行相同操作
def partition(nums, start, end):
    pivot = nums[end]
    # 应用双指针完成分类
    i, j = start, end-1
    while i < j:
        if nums[i] <= pivot:
            i += 1
        elif nums[j] > pivot:
            j -= 1
        else:
            nums[i], nums[j] = nums[j], nums[i]
    # 结束分类，需要判断pivot的位置
    if nums[i] > pivot:
        nums[i], nums[end] = pivot, nums[i]
        return i
    else:
        return end
    
def quick_sort(nums, start, end):
    if start < end:
        pivot_pos = partition(nums, start, end)
        quick_sort(nums, start, pivot_pos-1)
        quick_sort(nums, pivot_pos+1, end)
    return nums

print(quick_sort(nums, 0, len(nums)-1))
