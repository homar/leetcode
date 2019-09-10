class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        first_second = first + " " + second
        first_second_len = len(first_second)
        N = len(text)
        current_index = 0
        i = 0
        result = []
        start = True
        while i < N:
            if text[i] == " ":
                start = True
            if (start or current_index > 0) and text[i] == first_second[current_index]:
                current_index = current_index + 1
                i = i + 1
                if current_index >= 1 and text[i - 1] != " ":
                    start = False
            else:
                if current_index > 0:
                    current_index = 0
                else:
                    i = i + 1
            if current_index == first_second_len and i < N and text[i] == " ":
                i = i + 1
                third = ""
                current_index = 0
                while i < N and text[i] != " ":
                    third = third + text[i]
                    if text[i] == first_second[current_index]:
                        current_index = current_index + 1
                    i = i + 1
                result.append(third)
                if current_index == 0:
                    start = False
        return result

s = Solution()

result = s.findOcurrences("alice is aa good girl she is a good student", "a", "good")
assert result == ["student"]

result = s.findOcurrences("ab ab cd ab", "ab", "cd")
assert result == ["ab"]

result = s.findOcurrences("tef oncms btfzzcws btfzzcws btfzzcws oncms tef btfzzcws tef tef oncms btfzzcws kym btfzzcws x btfzzcws tef x tef kym tef oncms oncms oncms x x kym tef btfzzcws x kym x x tef oncms kym btfzzcws oncms x oncms", "x", "oncms")
assert result == []

result = s.findOcurrences("alice is a good girl she is a good student", "a", "good")
assert result == ["girl","student"]

result = s.findOcurrences("we will we will rock you", "we", "will")
assert result == ["we","rock"]