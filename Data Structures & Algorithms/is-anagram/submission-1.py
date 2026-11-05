class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        dit1 = {}
        dit2 = {}

        for vals in s:
            if vals not in dit1:
                dit1[vals] = 1 
            else:
                dit1[vals] += 1 

        for valt in t:
            if valt not in dit2:
                dit2[valt] = 1 
            else:
                dit2[valt] += 1 


        if dit1 == dit2:
            return True
        else:
            return False