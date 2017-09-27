# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import random

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def createTree(self, h, n):
        if h > n:
            return None
        x1 = random.randint(0, 1000)
        x2 = random.randint(0, 1000)
        self.left = TreeNode(x1).createTree(h+1, n)
        self.right = TreeNode(x2).createTree(h+1, n)
        return self

class Solution(object):
    def calsum(self, root):
        global ans
        if root:
            x = root.val+(self.calsum(root.left) or 0)+(self.calsum(root.right) or 0)
            ans.append(x)
            return x

    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        global ans
        ans = []
        self.calsum(root)
        dict = {}
        maxnum = -float('inf')
        for i in ans:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
            maxnum = max(dict[i],maxnum)
        ans1 = []
        for i in dict:
            if dict[i] == maxnum:
                ans1.append(i)
        return ans1

s = Solution()
r = TreeNode(100)
r.createTree(0,1)
print(s.findFrequentTreeSum(r))