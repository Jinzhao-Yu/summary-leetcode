# 二分查找 Binary Search
- 一种针对**有序区间**内的 $O(logN)$ 的搜索方式，常用于已经排好序的Array
- 两大原则：
  - 每次都要缩减搜索区域 Shrink the search space every iteration
  - 每次缩减不能将潜在答案排除在外 Cannot exclude potential answers during each shrinking
- General code
  ```python
  l,r = 0,len(array)
  while l < r: # or l <= r or l < r-1 depends on problems
    mid = l + (r-l)/2 # or l + (r-l+1)/2
    if array[mid] == target:
      return mid
    elif array[mid] > target:
      r = mid-1 # or r = mid depends on problems
    else:
      l = mid+1 # or l = mid depends on problems
   return l
  ```
## Leetcode题目
- [ ] [1026.Longest Repeating Substring](https://leetcode.cn/problems/longest-repeating-substring/)
- [x] [410.Split Array Largest Sum](https://leetcode.cn/problems/split-array-largest-sum/)
- [ ] [1231.Divide Chocolate](https://leetcode.cn/problems/divide-chocolate/)
- [x] [852. Peak Index in a Mountain Array](https://leetcode.cn/problems/peak-index-in-a-mountain-array/)
- [x] [1011. Capacity To Ship Packages Within D Days](https://leetcode.cn/problems/capacity-to-ship-packages-within-d-days/)
- [ ] [1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold](https://leetcode.cn/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/)
