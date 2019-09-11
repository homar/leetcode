class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 0
        elif N == 1:
            return 1
        else:
            a = 1
            b = 0
            i = 1
            while i < N:
                tmp = a
                a += b
                b = tmp
                i += 1
        return a

s = Solution()

result = s.fib(2)
assert result == 1

result = s.fib(3)
assert result == 2

result = s.fib(4)
assert result == 3
