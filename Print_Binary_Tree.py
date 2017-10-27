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
    def caldepth(self, r, depth):
        global maxlayer
        if depth > maxlayer :
            maxlayer = depth
        if r.left :
            self.caldepth(r.left, depth+1)
        if r.right :
            self.caldepth(r.right, depth+1)
        return None

    def constructans(self, r, depth, k, midnow):
        global ans, maxlayer
        j = 0
        if k < 0 :
            j = midnow - 2**(maxlayer-depth)
        elif k > 0:
            j = midnow + 2**(maxlayer-depth)
        elif k == 0:
            j = midnow
        ans[depth][j] = str(r.val)
        if r.left :
            self.constructans(r.left, depth+1, -1, j)
        if r.right :
            self.constructans(r.right, depth+1, 1, j)
        return None

    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        global maxlayer, ans
        maxlayer = -float('inf')
        ans = []
        self.caldepth(root, 0)
        n = maxlayer + 1
        m = 2**n - 1
        mid = m // 2
        ans = [[""]*m for _ in range(0, n)]
        self.constructans(root, 0, 0, mid)
        return ans

s = Solution()
r = TreeNode(100).createTree(0, 3)
print(s.printTree(r))



