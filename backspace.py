# Example 1:

# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".

class Solution(object):
    def backspaceCompare(self, S, T):
     # S = "ab##", T = "c#d#" , result = ""

        i=0
        while(S!='' and i<len(S)):
            if i==0 and S[0]=="#":
                print(S[0])
                # S=S.replace(S[0],'')
                S = S[i+1:]
                print("if",S)
                i=0
            elif S[i]=="#":
                S=S.replace(S[i-1:i+1],'')
                print("elif",S)
                i=0
            else:
                i+=1
        print(S)
        print("-----")
        i=0
        while(T!='' and i<len(T)):
            if i==0 and T[0]=="#":
                T = T[i+1:]
                print("if",T)
                i=0
            elif T[i]=="#":
                T=T.replace(T[i-1:i+1],'')
                print("elif",T)
                i=0
            else:
                i+=1
        print(T)
        if S==T:
            return True
        else:
            return False

        