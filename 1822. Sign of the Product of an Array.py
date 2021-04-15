class Solution:
    def arraySign(self, nums: List[int]) -> int:
        """
        There is a function signFunc(x) that returns:

        1 if x is positive.
        -1 if x is negative.
        0 if x is equal to 0.

        You are given an integer array nums. Let product be the product of all values in the array nums.

        Return signFunc(product)
        """

        # odd wording
        # write signFunc()?

        # Integers in Python are treated as arbitrary precision two's complement values
        # python seems to be odd in regards to bits and their manipulation regarding sign
        # could: use a bitmask of size(int)

        # simple
        # iterate and update sign?
        sign = 1
        for n in nums:
            if n > 0:
                pass
            elif n < 0:
                sign = -sign
            else:
                return 0

        return sign