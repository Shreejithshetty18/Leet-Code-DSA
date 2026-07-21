class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        s = set()

        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total == 0:
                    s.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1

                elif total > 0:
                    k -= 1

                else:
                    j += 1

        return [list(x) for x in s]