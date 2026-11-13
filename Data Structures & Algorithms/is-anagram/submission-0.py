class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        tempS, tempT = {}, {}
        for i in range(len(t)):
            tempS[s[i]] = 1 + tempS.get(s[i],0)
            tempT[t[i]] = 1 + tempT.get(t[i],0)
        for x in tempS:
            if tempS[x] != tempT.get(x,0):
                return False
        return True
        
    
        
        