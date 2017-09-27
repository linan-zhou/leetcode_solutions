class MapSum(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.dict[key] = val
        return None

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        ans = 0
        for i in self.dict:
            if i.startswith(prefix):
                ans += self.dict[i]
        return ans
