import random
# Definition for a binary tree node.

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
    def inordertravel(self,rt):
        a = []
        b = []
        ans = []
        if not rt:
            return None
        if rt.left:
            a = self.inordertravel(rt.left)
        ans = a + [rt.val]
        if rt.right:
            b = self.inordertravel(rt.right)
        ans = ans + b
        return ans
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root:
            return self.inordertravel(root)
        else:
            return []

t = TreeNode(1).createTree(0,3)
print(Solution().inorderTraversal(t))