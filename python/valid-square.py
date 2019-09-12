class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        points = [p1, p2, p3, p4]
        points.sort(key=lambda x: x[0])
        top_left = points[0]
        bottom_left = points[1]
        if points[1][1] > points[0][1]:
            top_left = points[1]
            bottom_left = points[0]
        top_right = points[2]
        bottom_right = points[3]
        if points[3][1] > points[2][1]:
            top_right = points[3]
            bottom_right = points[2]
        result = True
        if not (self.calculate_length(top_left[0], top_left[1], bottom_left[0], bottom_left[1]) == self.calculate_length(top_right[0], top_right[1], bottom_right[0], bottom_right[1]) and self.calculate_length(top_left[0], top_left[1], top_right[0], top_right[1]) == self.calculate_length(bottom_left[0], bottom_left[1], bottom_right[0], bottom_right[1]) and self.calculate_length(top_left[0], top_left[1], bottom_left[0], bottom_left[1]) == self.calculate_length(top_left[0], top_left[1], top_right[0], top_right[1])) or self.calculate_length(top_left[0], top_left[1], bottom_left[0], bottom_left[1]) == 0:
            result = False
        if not (self.calculate_length(top_left[0], top_left[1], bottom_right[0], bottom_right[1]) == self.calculate_length(top_right[0], top_right[1], bottom_left[0], bottom_left[1])):
            result = False
        return result

    def calculate_length(self, p10, p11, p20, p21):
        result = (p10 - p20)*(p10 - p20) + (p11 - p21)*(p11 - p21)
        return result

s = Solution()
result = s.validSquare([0,0], [1,1], [1,0], [0,1])
assert result == True

result = s.validSquare([0,0], [0,0], [0,0], [0,0])
assert result == False
