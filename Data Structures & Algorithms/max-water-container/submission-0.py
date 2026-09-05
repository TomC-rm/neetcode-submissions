class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_volume = 0 # initialize max volume
        
        while left < right: 

            # calculate current volume
            width = right - left
            height = min(heights[left], heights[right])
            current_volume = width * height

            # update max volume
            max_volume = max(max_volume, current_volume)

            # choose the indice to move (the smallest one)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return max_volume
            