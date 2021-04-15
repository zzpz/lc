class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        """
        Given an array of integers nums.

        A pair (i,j) is called good if nums[i] == nums[j] and i < j.

        Return the number of good pairs.
        """

        # simplest
        """
        O(n * (n-1)) run time
        rval = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and i < j:
                    rval+=1
        return rval
        """

        # optimising?
        """
        O(n+k) k distinct values
        
        # can we do it in O(n)?
        # only counts if i == j
            # count the number of each distinct number?
            
        # only counts if i < j 
            # means [1] -->0
            # [1, 1] --> 1
            # [1, 1,1] -> 1+1
            # [1, 1,1,1] -> 3+2+1
            # n*(n-1)//2

        """
        num_freq = {}  # functioning as a hashmap
        for i in range(len(nums)):
            # hashmap.put()
            num = nums[i]
            count = num_freq.get(num)

            if count is None:
                num_freq.update({num: 1})
            else:
                num_freq.update({num: count + 1})

        # list comp to iterate and sum
        good_pairs = sum([n * (n - 1) // 2 for n in num_freq.values()])

        return good_pairs  # [1, 1] --> 1
