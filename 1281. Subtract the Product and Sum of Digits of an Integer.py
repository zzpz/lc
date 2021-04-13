class Solution:
    def subtractProductAndSum(self, n: int) -> int:

        """
        Given an integer number n, return the difference between the product of its digits and the sum of its digits.

        Input: n = 234
        Output: 15
        Explanation:
        Product of digits = 2 * 3 * 4 = 24
        Sum of digits = 2 + 3 + 4 = 9
        Result = 24 - 9 = 15

        Constraints:
        1 <= n <= 10^5
        """

        # work from reverse using modulus to extract the end digit (%10)
        # remove that place (//10)
        # add and multiply
        
        p = 1
        s = 0
        
#         while n >0 :
#             d = n%10
#             p*=d
#             s+=d
            
#             n = n//10
    
#         return p - s
    

        # faster to convert from a string? 
        # repeated modulus and division slower than iterating?
        
        digits = []
        for d in str(n):
            digits.append(int(d))
            
        for d in digits:
            p*=d
            s+=d
        return p-s
