class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        ans = right

        while left <= right:

            k = left + (right - left) // 2

            total_hours = sum((p + k-1)//k for p in piles) #ex: p=4 k=5 -> p//k would have been 0 but p + k-1 = 8 // k == 1

            if total_hours > h:
                left = k + 1
            else:
                right = k - 1
                ans = k
        return ans