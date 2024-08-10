class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s=="":
            return True
        curr=0
        lenS=len(s)

        if lenS > len(t):
            return False
        for c in t:
            
            if(s[curr] == c):
                curr+=1
            if curr==lenS:
                return True
        return False
            


        