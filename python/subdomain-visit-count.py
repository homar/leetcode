class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        counter = {}
        for domain in cpdomains:
            pair = domain.split(" ")
            inc = int(pair[0])
            splitted = pair[1].split(".")
            N = len(splitted)
            i = N - 1
            while i >= 0:
                j = i
                current_domain = ""
                while j < N:
                    if j != i:
                        current_domain += "."
                    current_domain += splitted[j]
                    j += 1
                if current_domain in counter:
                    counter[current_domain] += inc
                else:
                    counter[current_domain] = inc
                i -= 1
        result = []
        for domain in counter:
            result.append("{} {}".format(counter[domain], domain))

        return result

s = Solution()

result = s.subdomainVisits(["9001 discuss.leetcode.com"])
assert "9001 discuss.leetcode.com" in result and "9001 leetcode.com" in result and "9001 com"in result