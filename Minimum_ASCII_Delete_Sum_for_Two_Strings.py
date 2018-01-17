class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        list1 = {}
        list2 = {}
        i = 1
        tot1 = 0
        tot2 = 0
        for x in s1:
            list1[i] = ord(x)
            tot1 += ord(x)
            i += 1
        i = 1
        for x in s2:
            list2[i] = ord(x)
            tot2 += ord(x)
            i += 1
        n = len(list1)
        m = len(list2)
        dp = [[0]*(m+1) for _ in range(0,(n+1))]
        for i in list1:
            for j in list2:
                if list1[i] == list2[j]:
                    if (i-1>=0) and (j-1>=0):
                        dp[i][j] = dp[i-1][j-1] + list1[i]
                if list1[i] != list2[j]:
                    a = 0
                    b = 0
                    if (i-1 >= 0):
                        a = dp[i-1][j]
                    if (j-1 >= 0):
                        b = dp[i][j-1]
                    dp[i][j] = max(a, b)
        # for i in dp:
        #     print(i)
        sum = dp[n][m]
        ans = tot1 + tot2 - 2*sum
        return ans

s = Solution()
print(s.minimumDeleteSum('sea','eat'))