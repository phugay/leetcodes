# s = "leetcode"
# return 0.

# s = "loveleetcode",
# return 2.

class Solution(object):
    def firstUniqChar(self, s):
        d = {}
        inds = []
        if s=="" or s==" ":
            return -1
        elif len(s)==1:
            return 0
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]]+=1
            else:
                d[s[i]]=1
        for k in d:
            if d[k]==1:
                if k in s:
                    index = s.find(k)
                    inds.append(index)
            else:
                inds.append(-1)
        inds = sorted(set(inds))
        print(inds)
        if len(inds)==1:
            return -1
        elif inds[0]==-1:
            return (inds[1])
        else:
            return (inds[0])
        