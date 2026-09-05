class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            while left < right:
                sum_triplet = nums[i] + nums[left] + nums[right]
                if sum_triplet < 0:
                    left += 1
                elif sum_triplet > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left+1] == nums[left]:
                        left += 1
                    while left < right and nums[right-1] == nums[right]:
                        right -= 1
                    left += 1
                    right -= 1
                
        return res
