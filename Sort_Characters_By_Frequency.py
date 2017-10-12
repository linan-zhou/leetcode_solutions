class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dict = {}
        for x in s:
            if x in dict:
                dict[x] += 1
            else:
                dict[x] = 1
        ans =''
        dict1 = sorted(dict.items(), key=lambda a:a[1], reverse=True)
        for x in dict1:
            ans += x[0]*x[1]
        return ans

s = Solution()
print(s.frequencySort('aaaffFFFF'))

