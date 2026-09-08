class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:

            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            # if the left side is sorted
            elif nums[left] <= nums[mid]: 
                # if target is in left search left
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                # else search right
                else:
                    left = mid + 1
            
            # right side is sorted
            else:
                # if target is right search right
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                #else search left:
                else:
                    right = mid - 1
        return -1


