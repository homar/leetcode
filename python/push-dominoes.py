class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        N = len(dominoes)
        forces = [0] * N
        force = 0
        for i in range(N):
            if dominoes[i] == 'R':
                force = N
            elif dominoes[i] == 'L':
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] += force
        force = 0
        for i in range(N-1, -1, -1):
            if dominoes[i] == 'L':
                force = N
            elif dominoes[i] == 'R':
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] -= force
        result = ""
        for i in range(N):
            if forces[i] > 0:
                result = result + 'R'
            elif forces[i] == 0:
                result = result + '.'
            else:
                result = result + 'L'
        return result

s = Solution()
result1 = s.pushDominoes("RR.L")
print result1
assert  result1 == "RR.L"
result2 = s.pushDominoes(".L.R...LR..L..")
print result2
assert  result2 == "LL.RR.LLRRLL.."
