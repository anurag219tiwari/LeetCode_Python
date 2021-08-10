"""
Used Kadane's Algorithm
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #kadane's algorithm
        max_sum = nums[0]
        j = 0
        for i in range(len(nums)):
            if nums[i] >= sum(nums[j:i+1]):
                current_sum = nums[i]
                j = i
            else:
                current_sum = sum(nums[j:i+1])
            if current_sum>max_sum:
                max_sum = int(current_sum)
        return max_sum
        
