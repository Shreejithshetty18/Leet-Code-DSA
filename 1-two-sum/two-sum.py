class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h={}
        ans=[]
        for i in range(0,len(nums)):
            x=target-nums[i]
            if x in h:
                ans.append(i)
                ans.append(h.get(x))
                return ans
            h[nums[i]]=i
        return None
        