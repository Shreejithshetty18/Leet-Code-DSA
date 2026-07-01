class Solution:
    def mergeAlternately(self, a: str, b: str) -> str:
        c=""
        i=0 #string a
        j=0 #string b
        pick=0
        
        while i<=len(a)-1 and j<=len(b)-1:
            if(pick==0):
                c=c+a[i]
                i=i+1
                pick=1
            else:
                c=c+b[j]
                j=j+1
                pick=0

        while i<=len(a)-1:
            c=c+a[i]
            i=i+1

        while j<=len(b)-1:
            c=c+b[j]
            j=j+1
        return c





