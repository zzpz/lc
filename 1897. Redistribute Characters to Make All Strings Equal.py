class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        """
        You are given an array of strings words (0-indexed).

        In one operation, pick two distinct indices i and j, where words[i] is a non-empty string, and move any character from words[i] to any position in words[j].

        Return true if you can make every string in words equal using any number of operations, and false otherwise.


        1 <= words.length <= 100
        1 <= words[i].length <= 100
        words[i] consists of lowercase English letters


        Args:
            words: A list of 1 to 100 words of length 1 to 100.


        Returns:
            bool

        Raises:
            None

        """

        ######
        # Naive Solution
        # for each letter if count(leter) % count(words) !0 -> false
        ######

        letters_map = {}

        for word in words:
            for letter in word:
                count = letters_map.get(letter)

                if count is None:
                    letters_map.update({letter: 1})
                else:
                    letters_map.update({letter: count + 1})

        for letter, count in letters_map.items():
            if count % len(words) != 0:
                return False

        return True

        # incorrect solution below

        # misread problem statement, words must be equal, not just equal length.
        # same principle applies, only now it applies to counts of letters and sum of letters.
        # considerations
        # cannot be done if count of all letters is odd
        # possible substitution of the problem with even/odd of words
        # e.g. 3 even,2 odd, can it be done? no?
        # 2,2,2,1,1 no
        # 3,3,3,2,2 no
        # base case:
        # 1 word
        # true always
        # 2 words
        # true if both even / both odd
        # true if even count is even, and odd count is even
        # 3 words
        # 1,1,7     odd= 3
        # -->  9  --> 3,3,3
        # 1,1,3 --> odd = 3
        # --> 5  no
        # 4,2,5     even = 2
        # --> 11 no
        # sum == prime --> no
        # sum % count != 0 --> false
        # n words
        # e,e,e,o,o     e=3,o=2
        # --> 2,2,4,3,1
        # 12 % 5 --> no
        # e,e,o,o,o
        # --> 2,4,3,3,3
        # 15 --> yes
        # --> 2,2,1,1,1
        # 7 -- > no

        #######
        # Naive solution
        # if sum % count != 0 --> false
        #######

        # wordsum = sum([len(word) for word in words] )
        # wordcount = len(words)

        # if wordsum % wordcount == 0:
        #     return True

        # return False
