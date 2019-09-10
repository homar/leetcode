class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        map = {}
        i = 0
        N = len(nums)
        while i < N:
            if nums[i] in map:
                for x in map[nums[i]]:
                    if abs(x - i) <= k:
                        return True
                current_list = map[nums[i]]
                current_list.append(i)
                map[nums[i]] = current_list
            else:
                map[nums[i]] = [i]
            i += 1
        return False

s = Solution()
result = s.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2)
assert result == False


result = s.containsNearbyDuplicate([1, 2, 3, 1], 3)
assert result == True

result = s.containsNearbyDuplicate([1, 0, 1, 1], 1)
assert result == True

