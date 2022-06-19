class Solution:
    def greatestLetter(self, s: str) -> str:
        d={}
        for i in s:
            d[i]=1
        for i in range(25,-1,-1):
            if d.get(chr(ord('a')+i)) and d.get(chr(ord('A')+i)):
                return chr(ord('A')+i)
        return ""
        
