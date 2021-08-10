"""
My approach
Used an algorithm counting sort to solve the problem
"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #counting_sort
        c = [0]*3
        b = [0]*(len(nums)+1)
        for i in range(len(nums)):
            c[nums[i]] = c[nums[i]] + 1
        for i in range(1,3):
            c[i] = c[i] + c[i-1]
        for i in range(len(nums)-1,-1,-1):
            b[c[nums[i]]] = nums[i]
            c[nums[i]] -= 1
        b.pop(0)
        nums[:] = bfg
