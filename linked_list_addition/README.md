## You are given two linked-lists representing two non-negative integers.  Add the two numbers and return it as a linked list.

### Approach:
 - Over write python's dunder method \__add__ to accept a new linked list and perform the 
   mathematical addition on each and every node in the linked lists.
    - Reverse the first linked list as the addition should start from lsb
      <br />Time Complexity(__O__(n)) => n
    - Reverse the second linked list as the addition should start from lsb
      <br />Time Complexity(__O__(n)) => n
    - Start traversing both the linked lists at same time till both gets exhaust
      <br />Time Complexity(__O__(n)) => n
    - while traversing, add both node's values and create a new node with result value
      and store carry forward in a new variable.
    - Add this newly created node to the new linked list
    - Reverse the linked list so that the head will point to msb instead of lsb
      <br />Time Complexity(__O__(n)) => n
 - Time Complexity(__O__(n)) => n + n + n +n = 4n
 
### How to Run:
* Add algos folder to python path and run below commands
```python
from linked_list_addition import Node, SingleLinkedList
Node(10, Node(11)) # creates a Node
linked_list = SingleLinkedList() # creates a linked list
linked_list.add(Node(2)) # adds a node to linked list
```

* How to add two linked lists

```python
from linked_list_addition import Node, SingleLinkedList
>>> linked_list = SingleLinkedList()

>>> linked_list.add(Node(1))
Head: 1
Pointer: 1
Length: 1
LinkedList: 1

>>> linked_list.add(Node(2))
Head: 1
Pointer: 2
Length: 2
LinkedList: 1->2

>>> linked_list.add(Node(3))
Head: 1
Pointer: 3
Length: 3
LinkedList: 1->2->3

>>> linked_list.add(Node(4))
Head: 1
Pointer: 4
Length: 4
LinkedList: 1->2->3->4

>>> print (linked_list)
Head: 1
Pointer: 4
Length: 4
LinkedList: 1->2->3->4

>>> linked_list2 = SingleLinkedList()

>>> linked_list2.add(Node(4))
Head: 4
Pointer: 4
Length: 1
LinkedList: 4

>>> linked_list2.add(Node(8))
Head: 4
Pointer: 8
Length: 2
LinkedList: 4->8

>>> print (linked_list2)
Head: 4
Pointer: 8
Length: 2
LinkedList: 4->8

>>> new_linked_list = linked_list + linked_list2

>>> print (new_linked_list)
Head: 1
Pointer: 2
Length: 4
LinkedList: 1->2->8->2
```
   
 


