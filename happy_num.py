# Write an algorithm to determine if a number n is "happy".

# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

# Return True if n is a happy number, and False if not.

class Solution(object):     

    def isHappy(self, n):
        # a = self.opers(n)
        # return a
        sums = []
        while(n!=1):
            strnum = str(n)
            numlist = list(strnum)
            sumnums = 0
            for i in range(len(numlist)):
                numlist[i]=int(numlist[i])**2
                sumnums += numlist[i]
            n = sumnums
            if sumnums not in sums:
                sums.append(sumnums)
            else:
                return False            
        if(n==1):
            return True
            
