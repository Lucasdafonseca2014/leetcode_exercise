"""
Exercício proposto no site leetcode:

link útil para "linked list": https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm

Projeto utilizando controle de versionamento GIT
"""


class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


class Solution:

    @staticmethod
    def add_twonumbers(l1: ListNode, l2: ListNode):

        l_1 = []
        atual = l1
        while atual is not None:
            l_1.append(atual.val)
            atual = atual.next

        l_1.reverse()
        e1 = Solution.list_int(l_1)

        l_2 = []
        atual = l2
        while atual is not None:
            l_2.append(atual.val)
            atual = atual.next

        l_2.reverse()
        e2 = Solution.list_int(l_2)

        final = Solution.int_listnode(e1, e2)

        print('Resultados:')

        Solution.print_listnode(l1)
        Solution.print_listnode(l2)
        Solution.print_listnode(final)

        return final

    @staticmethod
    def list_int(li: list):

        i = ''
        for n in li:
            i = i + str(n)
        i = int(i)
        return i

    @staticmethod
    def int_listnode(i1: int, i2: int) -> ListNode:
        e = list(str(i1 + i2))
        e.reverse()

        lis_ = []
        for element in e:
            ln = ListNode(element)
            lis_.append(ln)

        anterior = lis_[0]
        for element in lis_[1:]:
            atual = element
            anterior.next = atual
            anterior = atual

        return lis_[0]

    @staticmethod
    def print_listnode(e1: ListNode):

        atual = e1
        while atual is not None:
            print(f'{atual.val} -> ' if atual.next is not None else f'{atual.val}', end=' ')
            atual = atual.next
        print()


if __name__ == '__main__':

    n1_e1 = ListNode(2)
    n1_e2 = ListNode(4)
    n1_e3 = ListNode(3)
    n2_e1 = ListNode(5)
    n2_e2 = ListNode(6)
    n2_e3 = ListNode(4)
    n1_e1.next = n1_e2
    n1_e2.next = n1_e3
    n2_e1.next = n2_e2
    n2_e2.next = n2_e3
    r = Solution.add_twonumbers(n1_e1, n2_e1)
