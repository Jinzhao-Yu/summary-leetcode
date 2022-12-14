  # 双指针 Two Pointers

## 同向双指针
![image](https://github.com/Jinzhao-Yu/summary-leetcode/blob/0152dcbc06eb7eaa216a7b8fe77dc0417176beb7/%E5%8F%8C%E6%8C%87%E9%92%88/Figure/TwoPointers1.png)
- 图中所示`[0,i)`为处理好的数据，`[i,j)`为处理过但并不需要的数据，`[j,n)`为还未处理的数据，其中区间的开闭需要考虑题目具体情况；
- 同向双指针的优点在于**可以保持处理好的数据原有的相对位置**：
  - `[1,2,0,3,8,0]` moves zeros to the end
  - result: `[1,2,3,8,0,0]` 保持了非零元素的相对位置
- 通用步骤：
  - initialize two pointers `i,j`, generally both 0,
  - while `j < n`:
    - if `array[j]` is needed, we assign `array[i] = array[j]`, then move both `i` and `j` forward,
    - else keep `i` at the same position, and move `j` forward

## 反向双指针
![image](https://github.com/Jinzhao-Yu/summary-leetcode/blob/d2b0d5aba92bdd681d516ba397f5b8ed4c070774/%E5%8F%8C%E6%8C%87%E9%92%88/Figure/TwoPointers2.png)
- 图中所示`[0,i)`和`(j,n)`均为处理好的数据，`[i,j]`为还未处理的数据，其中区间的开闭需要考虑题目具体情况；
- 通用步骤：
  - initialize two pointers `i,j` as `0` and `n-1`,
  - while `i <= j`:
    - based on the problem, decide what to do with `array[i]` and `array[j]`
    - move at least 1 pointer forward in its own direction
 
## Leetcode题目
- [x] [344.Reverse String](https://leetcode.cn/problems/reverse-string/)
- [x] [26. Remove Duplicates from Sorted Array](https://leetcode.cn/problems/remove-duplicates-from-sorted-array/)
- [x] [11. Container With Most Water](https://leetcode.cn/problems/container-with-most-water/)
- [ ] [42. Trapping Rain Water](https://leetcode.cn/problems/trapping-rain-water/)
- [x] [283. Move Zeroes](https://leetcode.cn/problems/move-zeroes/)
- [ ] [80. Remove Duplicates from Sorted Array II](https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/)
- [ ] [1047. Remove All Adjacent Duplicates In String](https://leetcode.cn/problems/remove-all-adjacent-duplicates-in-string/)
