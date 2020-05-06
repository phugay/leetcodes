# Input: 5
# Output: 2
# Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

class Solution(object):
    def findComplement(self, num):
        rem=0
        binstr = ""
        xorstr = ""
        if num == 1:
            return 0
        while(num!=0):
            rem = num%2
            num = num/2
            binstr=binstr+str(rem)
        binstr=binstr[::-1]
        # final = int(binstr)
        for i in range(len(binstr)):
            xorstr = xorstr+"1"        
        val = int(binstr,2) ^ int(xorstr,2)
        return(val)
        