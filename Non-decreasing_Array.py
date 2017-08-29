class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        f = 0
        n = len(nums)
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                f += 1
                if f > 1:
                    return False
                if (i + 1 < n) and (i - 2 >= 0) and (nums[i + 1] < nums[i - 1]) and (nums[i] < nums[i-2]):
                    return False
        return True