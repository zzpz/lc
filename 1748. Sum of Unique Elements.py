class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        """
        You are given an integer array nums.
        The unique elements of an array are the elements that appear exactly once in the array.

        Return the sum of all the unique elements of nums.
        """

        # simple
        # O(2n)

        """
        
        uniq = {}
        rval = 0
        for n in nums:
            if n not in uniq: #O(1)
                uniq.update({n:True})
            else:
                uniq.update({n:False})
       
        
        for k,v in uniq.items(): #O(n)
            if v == True:
                rval+=k
        
        return rval
        """
        # optimise?
        """
        # direct index the dict vals, don't check 'if in'
        
        unique = {}
        out = 0
        for n in nums:
            unique[n] = unique.get(n,0)+1 #get and update
        
        for k,v in unique.items():
            if v ==1:
                out+=k
        
        return out
        """
        # cleaner -->  use Counter() to build the count dict
        out = 0
        c = Counter(nums)
        for k, v in c.items():
            if v == 1:
                out += k
        return out