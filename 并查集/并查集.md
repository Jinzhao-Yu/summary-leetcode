# 并查集
## 基本概念
- 并查集是一种数据结构
- 并查集这三个字，一个字代表一个意思
- 并（Union），代表合并
- 查（Find），代表查找
- 集（Set），代表这是一个以字典为基础的数据结构，它的基本功能是合并集合中的元素，查找集合中的元素
- 并查集的典型应用是有关连通分量的问题
- 并查集解决单个问题（添加，合并，查找）的时间复杂度都是 $O(1)$
- 因此，并查集可以应用到**在线算法**中
## Class模版
实际上我们可以通过定义一个`Union_Find`的Class用于解决并查集的问题，本质上并查集需要记录的是每个节点的父节点：
```Python
class Union_Find(object):
  def __init__(self):
    self.father = {} #以字典形式存储
```
需要定义的函数包括**添加新节点(add)**、**查找节点祖先(find)**、**判断两节点是否连通(is_connected)**及**合并两个节点(merge)**
```Python
  def add(self,x):
    if x not in self.father:
      self.father[x] = None #新节点无父节点
			
  def find(self,x):
    root = x
    while self.father[root] != None:
      root = self.father[root]
    # 路径压缩，即只记录祖先情况将树的深度压缩为2
    while x != root:
      original_father = self.father[x]
      self.father[x] = root
      x = original_father
    return root

  def is_connected(self,x,y):
    return self.father[x] == self.father[y]
  
  def merge(self,x,y):
    root_x,root_y = self.find(x),self.find(y)
    if root_x != root_y: #还没有完成合并或祖先不同
      self.father[root_x] = root_y # 交换也是一样的
```
## 结合题目
需要结合题目进行条件的改变或增加attributes，例如计算连通集数量时需要添加一个`self.nums_of_set = 0`，并在`add`时+1，`merge`时-1；
## Leetcode题目
- 模版题
  - [ ] [261. Graph Valid Tree](https://leetcode.cn/problems/graph-valid-tree/)
- 在线计算
