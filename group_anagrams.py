# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]

class Solution(object):
    def groupAnagrams(self, strs):
        groups = collections.defaultdict(list)
        for i in strs:
            groups[tuple(sorted(i))].append(i)
        return groups.values()
            
        
        
                
                
                
                                
                
        

                
                
                    