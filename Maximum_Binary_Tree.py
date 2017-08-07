# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        maxnum = -1
        for x in nums:
            if x > maxnum:
                maxnum = x
        mid = nums.index(maxnum)
        root = TreeNode(maxnum)
        if mid > 0:
            root.left = self.constructMaximumBinaryTree(nums[:mid])
        else:
            root.left = None
        if mid < len(nums)-1:
            root.right = self.constructMaximumBinaryTree(nums[mid+1:])
        else:
            root.right = None
        return root