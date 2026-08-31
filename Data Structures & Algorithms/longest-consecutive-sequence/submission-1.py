class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_sequence = 0

        for num in nums:
            current_sequence = 1

            if not num - 1 in nums_set:
                while num + 1 in nums_set:
                    current_sequence += 1
                    num += 1
            max_sequence = max(max_sequence, current_sequence)
        
        return max_sequence