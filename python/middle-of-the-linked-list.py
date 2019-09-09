# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        lenght = 0
        current = head
        while current != None:
            lenght = lenght + 1
            current = current.next

        if lenght < 2:
            return head
        result = head
        counter = 1
        while counter <= lenght / 2:
            result = result.next
            counter = counter + 1

        return result

x1 = ListNode(1)
x2 = ListNode(2)
x1.next = x2
x3 = ListNode(3)
x2.next = x3

s = Solution()

result = s.middleNode(x1)
assert result == x2

x4 = ListNode(4)
x3.next = x4

result = s.middleNode(x1)
assert result == x3