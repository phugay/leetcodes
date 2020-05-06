# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.


class Solution(object):
    def majorityElement(self, nums):
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in d:
            if d[i]>(len(nums)/2):
                print(i)
                return(i)
        