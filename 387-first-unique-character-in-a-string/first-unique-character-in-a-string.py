class Solution:
    def firstUniqChar(self, s: str) -> int:
        h={}
        for i in s:
            if i in h.keys():
                count=h[i]
                count=count+1
                h[i]=count

            else:
                h[i]=1

        for i in range(len(s)):
            if h[s[i]]==1:
                return i
        return -1
        