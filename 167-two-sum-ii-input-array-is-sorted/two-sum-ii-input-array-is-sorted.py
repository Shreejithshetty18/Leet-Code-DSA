class Solution:
    def twoSum(self, a: List[int], target: int) -> List[int]:
        i=0
        j=len(a)-1
        ans=[]
        while(i<j):
            if(a[i]+a[j]==target):
                ans.append(i+1)
                ans.append(j+1)
                return ans
               
            elif(a[i]+a[j]>target):
                j-=1
            else:
                i+=1

  