## Leetcode project

Resolução do desafio 2 proposto pelo site leetcode.
O exercício consiste em criar uma classe que manipule objetos do tipo "linked-list". A classe deve aceitar como 
argumentos 2 objetos "linked-list" representando números inteiros (ex: 456), inverter a ordem dos digitos dos dois 
objetos, realizar a soma, desfazer a inversão e depois retornar o valor em um objeto "linked-list".

exemplo:

~~~~
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
~~~~

Exemplo da classe linked-list:

~~~~
class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_
~~~~
 ### links importantes:
 
 Leetcode: https://leetcode.com/problems/add-two-numbers/
 
 Linked-list: https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm
 
