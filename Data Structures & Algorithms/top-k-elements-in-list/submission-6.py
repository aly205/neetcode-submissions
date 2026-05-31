class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = dict()
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse = True)    
        keys, values = zip(*sorted_counts)
        return list(keys[:k])
