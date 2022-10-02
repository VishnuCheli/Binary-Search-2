#Time Complexity:: Average: O(logn)=shortening search space using Binary Search, to move towards peak
#Space Complexity:: O(1) Not using any extra space.
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return 0
        l=0
        h=len(nums)-1
        
        while(l<=h):
            mid=l+(h-l)//2
            
            if(mid==0 or nums[mid-1]<nums[mid]) and (mid==len(nums)-1 or nums[mid]>nums[mid+1]):
                return mid
            elif(mid>0 and nums[mid-1]>nums[mid]):
                h=mid-1
            else:
                l=mid+1
            
