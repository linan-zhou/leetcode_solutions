class MagicDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dictionary = []

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        self.dictionary = dict

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        n = len(word)
        for s in self.dictionary:
            if n == len(s):
                tot = 0
                for i in range(0, n):
                    if word[i] != s[i]:
                        tot += 1
                if tot == 1:
                    return True
        return False

        # Your MagicDictionary object will be instantiated and called as such:
        # obj = MagicDictionary()
        # obj.buildDict(dict)
        # param_2 = obj.search(word)
s = MagicDictionary()
s.buildDict(['akfhkgl', 'kitty'])
print(s.search('katti'))