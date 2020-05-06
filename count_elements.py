# check if i and i+1 in same array

class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count = 0
        
        for i in arr:
            if i in arr and (i+1) in arr:
                count+=1
        return count