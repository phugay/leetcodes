
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pointer = 0
        for i,v in enumerate(nums):
            if v!=0:
                nums[pointer]=v
                pointer+=1
        while(pointer<len(nums)):
            nums[pointer]=0
            pointer+=1
            
                
            
                
            
                