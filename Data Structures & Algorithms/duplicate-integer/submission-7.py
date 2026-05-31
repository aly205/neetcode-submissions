class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        entries = set()
        for i in nums :
            if ( i in entries ):
                return True
            else:
                entries.add(i)
        return False