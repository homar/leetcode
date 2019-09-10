class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        min = 10000
        max = 0
        for i in A:
            if i > max:
                max = i
            if i < min:
                min = i
        diff = max - min
        diff_after_subtraction = diff - (2 * K)
        if diff_after_subtraction < 0:
            return 0
        else:
            return diff_after_subtraction

s = Solution()

result = s.smallestRangeI([4103, 2214, 5569, 6335, 4244, 9485, 7545, 8323, 7841, 8858], 391)
assert result == 6489

result = s.smallestRangeI([2, 7, 2], 1)
assert result == 3

result = s.smallestRangeI([1], 0)
assert result == 0

result = s.smallestRangeI([0, 10], 2)
assert result == 6

result = s.smallestRangeI([1, 3, 6], 3)
assert result == 0