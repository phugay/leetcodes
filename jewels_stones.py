# Input: J = "aA", S = "aAAbbbb"
# Output: 3

class Solution(object):
    def numJewelsInStones(self, J, S):
        jcount = 0
        for stone in S:
            if stone in J:
                jcount+=1
        return(jcount)
            
        
        