#Given a non-empty array of integers, every element appears twice except for one. Find that single one.


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count_of_nums = {}
        count = 1
        for i in nums:
            try:
                count_of_nums[i] = count_of_nums[i]+count
            except:
                count_of_nums[i] = count
        for i in count_of_nums:
            if count_of_nums[i]==1:
                print(i)
                return i
            
        