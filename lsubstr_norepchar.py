# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        newstr = ""
        a = ""
        final=""
        strs = []
        if s=="":
            return 0
        elif len(s)==1:
            return 1
        for i in s:
            if i not in newstr and i!=a:
                # print("not in newstr and not last char")
                newstr = newstr+i
                strs.append(newstr)
            elif i in newstr and i==newstr[-1]:
                # print("in newstr and last char")
                newstr= i
            elif i in newstr and i!=newstr[-1]:
                # print("in newstr and not last char")
                pos=newstr.find(i)
                newstr = newstr[pos+1:]+i
            a=i
            # print(strs,newstr)
        final=max(strs, key=len)
        print(final)
        return(len(final))