class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        https://stackoverflow.com/questions/3898572/what-is-the-standard-python-docstring-format

        Given an array of integers numbers that is **already sorted** in non-decreasing order, find two numbers such that they add up to a specific target number.

        Return the indices of the two numbers **(1-indexed)** as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.

        The tests are generated such that there is exactly one solution. You may not use the same element twice.

        runtime: O(n*Log(n)) --> for each, perform binary search

        Args:
            numbers: A list of increasing ints
            target: The target value

        Returns:
            A list of two indices in numbers such that they add to target.

        Raises:
            None
        """
        # numbers sorted
        # we can use binary search
        # exactly one solution
        # if n[x] doesn't match, all n[<x] wont match
        # can't use elements twice

        for i in range(len(numbers)):  # for each value in numbers
            left, right = i + 1, len(numbers) - 1  # bsearch indexes - excludes seen
            find = target - numbers[i]

            while left <= right:  # binary search
                mid = left + (right - left) // 2

                if numbers[mid] == find:  # found match
                    return [i + 1, mid + 1]  # return index of value (i, not left)
                elif numbers[mid] < find:  # halve to right
                    left = mid + 1
                else:
                    right = mid - 1  # halve to left


# return value is 1-indexed (e.g. index starts at 1)