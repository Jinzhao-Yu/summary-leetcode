# 链表Linked List
## Linked List V.S. Array
- Array: 一组内存里连续的数据
  - 能用index访问 $\rightarrow$ $O(1)$ Access
  - 添加元素直接添加在最后 $\rightarrow$ Amortized $O(1)$ Add（考虑到扩容）
  - 删除元素需要挪动后面所有元素位置 $\rightarrow$ $O(n)$ Delete
- Linked List: 内存里不一定连续的数据
  - 不能用index访问 $\rightarrow$ $O(n)$ Access
  - 添加元素添加在最后 $\rightarrow$ $O(n)$ Add，双链表 $O(1)$
  - 删除元素需要找到元素位置 $\rightarrow$ $O(n)$ Delete
## 方法：双指针Two Pointers
- 双指针指向Linked List节点，不再是index
- 双指针必定同向而行

**要点**
1. 双指针一个快一个慢，根据题目设置好相隔距离
2. 根据题目设置好两个指针移动速度
## 方法：递归Recursion
适用于解决**从后往前**的链表题目，因为Recursion本质上就是从后往前找结果的过程

**步骤Bottom up recursion 3 steps:**
1. Ask for subproblem result
2. Do something in current level of recursion
3. Return result

⚠️需要保证第1步和第3步返回的含义相同
## Leetcode
<details>
  <summary><a href="https://leetcode.cn/problems/reverse-linked-list/">206. Reverse Linked List</a></summary>

```python
  # Two pointers
  
```
</details>
