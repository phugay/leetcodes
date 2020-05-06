# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        maximum = -999
        if len(nums)==1:
            return nums[0]
        for v in nums:  
            if v>total:
                total=max(total+v,v)
                print("great ", total)
            elif v<total:
                if (total+v)>0:                    
                    total=max(total+v,v)
                else: 
                    total=max(total+v,v)
                print("less ", total)
            else:
                total=max(total+v,v)
            if maximum<total:
                maximum = total
        return maximum

#[1,2,-1,-2,2,1,-2,1,4,-5,4]
              
        
        