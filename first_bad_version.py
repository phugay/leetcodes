# Given n = 5, and version = 4 is the first bad version.

# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true

# Then 4 is the first bad version. 


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        start = 1
        end = n
        while(start<end):
            mid = start+(end-start)/2
            print(start, mid, end)
            if isBadVersion(mid)== True:
                print("true case")
                end = mid
            else:
                print("false case")
                start = mid+1
        return(start)
        

        