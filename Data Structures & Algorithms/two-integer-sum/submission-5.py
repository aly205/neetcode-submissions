class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_seen = dict()
        for (idx, num) in enumerate(nums):
            if (target - num in nums_seen):
                return [nums_seen[target - num], idx]
            else:
                nums_seen[num] = idx 
        