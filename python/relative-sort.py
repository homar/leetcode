class Solution(object):
    def relativeSortArray(self, a1, a2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        numbers = {}
        for i in a1:
            if i in numbers:
                numbers[i] += 1
            else:
                numbers[i] = 1
        index = 0
        for i in a2:
            for j in range(numbers[i]):
                a1[index] = i
                index += 1
            numbers[i] = 0
        rest = []
        for k in numbers:
            if numbers[k] != 0:
                for j in range(numbers[k]):
                    rest.append(k)
        rest.sort()
        for k in rest:
            a1[index] = k
            index += 1
        return a1

s = Solution()

result = s.relativeSortArray([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6])
assert result == [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]


