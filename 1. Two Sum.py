class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

        You may assume that each input would have exactly one solution, and you may not use the same element twice.

        Args:
            nums: the list of all values X from which target value can be made
            target: the target value T = X_i + X_j

        Returns:
            a list of 2 values that sum to target

        Notes:
            concept: reframe problem as X_j = T - X_i, store the unseen (X_j) value's and the current value's index
            big(O):   O(n)

        Raises:

        """
        # exactly one sol
        # can't use same element twice (index not int)

        # store a dict of the 'other side' of each pair seen
        unseen_Xj = {}

        for i, num in enumerate(nums):  # start with iterating each element nums[i]
            if num in unseen_Xj:
                return (
                    unseen_Xj[num],
                    i,
                )  # if we've already seen the other half of this value we can return that index + this index
            # else
            unseen_Xj[
                target - num
            ] = i  # add the other half we need to find with the index of the current half we have
