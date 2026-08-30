class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # use hashmap to count occurences for each number
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0) 
        
        # build bucket list
        freq = [[] for _ in range(len(nums) + 1)]
        for n, c in count.items():
            freq[c].append(n)
        
        # go through the bucket in reverse and return when len(res) == k
        res = []
        for b in range(len(freq) - 1, 0, -1):
            for num in freq[b]:
                res.append(num)
                if len(res) == k:
                    return res