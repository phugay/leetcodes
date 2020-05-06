# Each letter in the magazine string can only be used once in your ransom note.

# Note:
# You may assume that both strings contain only lowercase letters.

# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        flag = False     
        if ransomNote=="" and magazine=="":
            return True
        elif ransomNote=="" and magazine!="":
            return True 
        elif ransomNote!="" and magazine=="":
            return False
        for letter in ransomNote:
            if letter in magazine:
                magazine=magazine.replace(letter,"",1)
                flag=True
            else:
                flag=False                
                return(flag)
        return(flag)