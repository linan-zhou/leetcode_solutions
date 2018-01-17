class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        ans = 0
        for i in nums:
            if i in dict:
                continue
            label = nums.index(i)
            dict[label] = 1
            x = i
            tot = 1
            while (x != label):
                dict[x] = 1
                tot += 1
                x = nums[x]
            if tot > ans :
                ans = tot
            #print(tot)
        return ans

s = Solution()
print(s.arrayNesting([5,4,0,3,1,6,2]))