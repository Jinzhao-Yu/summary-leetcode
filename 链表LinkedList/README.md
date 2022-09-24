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
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
```
- 双指针方法
```python
  # Two pointers
  pre,cur = None,head
  while cur is not None:
    temp = cur.next #将当前节点的后面部分存下来
    cur.next = pre #将当前节点反向链接到上一个节点上
    pre,cur = cur,temp #更新上一个节点和当前节点的定义
  return pre
```
- Recursion迭代
```python
  # recursion
  # 本质上是从后往前对链表进行操作
  if head is None or head.next is None:
    return head

  reversed_list = self.reverseList(head.next) #将已经反转好的部分存下来
  head.next.next = head #将反转好的末尾节点与当前节点连起来
  head.next = None #将当前节点与下一个节点的链接断开
  return reversed_list
```
</details>
<details>
  <summary><a href="https://leetcode.cn/problems/delete-node-in-a-linked-list/">237. Delete Node in a Linked List</a></summary>
由于题目要求不使用链表的头节点，同时给出需要删除的是一个链表的形式，因此只需要在链表中找到需要删除的节点，将该节点的val改为下一个节点的val，再连接到下一个的下一个节点上即可

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
```
</details>
<details>
  <summary><a href="https://leetcode.cn/problems/linked-list-cycle/">141. Linked List Cycle</a></summary>
方法：快慢节点，如果快节点可以追上慢节点，证明存在循环

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 快慢节点
        if head is None:
            return False
        slow,fast = head,head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        
        return True
```
</details>
