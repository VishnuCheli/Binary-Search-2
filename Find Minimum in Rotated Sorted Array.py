#Time Complexity:: Average: O(logn) and lower. Shortening search space using Binary Search, and its a rotated sorted array.
#Space Complexity:: O(1) Not using any extra space.
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums)-1
        
        if nums[low]<nums[high] or len(nums)==1:
            return nums[0]
        
        
        while low<high:
            mid = low + (high-low)//2
            print(mid,low,high)
            if nums[mid] > nums[high]:
                low = mid+1
            else:
                high = mid
                
        return nums[low]