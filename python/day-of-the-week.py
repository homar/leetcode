class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        m = (month - 2) % 12
        if m == 0:
            m = 12
        D = (year % 10) + ((year / 10) % 10) * 10
        if month == 1 or month == 2:
            D -= 1
        C = year / 10 / 10
        f = (day + int((13*m-1)/5) + D + int(D/4) + int(C/4) - 2*C)

        return days[f % 7]

s = Solution()

result = s.dayOfTheWeek(29, 01, 2064)
assert result == "Tuesday"

result = s.dayOfTheWeek(29, 02, 2016)
assert result == "Monday"

result = s.dayOfTheWeek(31, 8, 2019)
assert result == "Saturday"

result = s.dayOfTheWeek(18, 7, 1999)
assert result == "Sunday"

result = s.dayOfTheWeek(15, 8, 1993)
assert result == "Sunday"