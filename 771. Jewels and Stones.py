class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        # list comp
#         sinj = [s for s in stones if s in jewels]
    
#         return len(sinj)
    
        # could make jewels an o(1) lookup and do it in o(n)
        j = 0
        for i in stones: #o(n)
            if i in jewels: #o(j)
                j +=1 #o(1)
        
        return j #O(nj)
    
