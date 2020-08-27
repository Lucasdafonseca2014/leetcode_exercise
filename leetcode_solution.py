class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


class Solution:
    def add_two_numbers(self, l1, l2, c=0):
        """

        :param l1: ListNode
        :param l2: ListNode
        :param c: ListNode
        :return: ListNode
        """
        val = l1.val + l2.val + c
        c = val // 10
        ret = ListNode(val % 10)

        if l1.next is not None or l2.next is not None or c != 0:
            if l1.next is None:
                l1.next = ListNode(0)
            if l2.next is None:
                l2.next = ListNode(0)
            ret.next = self.add_two_numbers(l1.next, l2.next, c)
        return ret
