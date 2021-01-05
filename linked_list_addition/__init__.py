from copy import deepcopy


class Node:
    """
        Description:
            Describes the Node in Data Structures, particularly w.r.t Single Linked List
    """
    def __init__(self, value, next_node=None):

        """
            Description:
                Initiator for the Node Object.
            :param value:
                Accepts any python object.
            :param next_node:
                Accepts a None or Node Type object
            :raises
                A type Error if neither next_node is an object of type Node
                nor None
                A type Error if the value is not an integer

            Examples:
                >>> from linked_list_addition import Node, SingleLinkedList

                >>> Node(10, Node(11))
                Node(value=10, next_node=Node(11))

                >>> Node(1)
                Node(value=1, next_node=None)

                >>> Node(10, 100)
                Traceback (most recent call last):
                  File "<input>", line 1, in <module>
                  File "C:\\Users\\gp\\Desktop\\algos\\linked_list_addition\\__init__.py", line 26, in __init__
                    raise TypeError("next_node accepts only Node type object.")
                TypeError: next_node accepts only Node type object.
                >>>
        """
        if not (isinstance(next_node, Node) or next_node is None):
            raise TypeError("next_node accepts only Node type object.")
        if not isinstance(value, int):
            raise TypeError("value accepts only integer type.")
        self.next_node = next_node
        self.value = value

    def __str__(self):
        """
        Description:
            String representation of Node
        :return:
            value of Node in String type.
        Examples:
            >>> node = Node(10)
            >>> print (node)
            10

            >>> node = Node(10, Node(100))
            >>> print (node)
            10
        """
        return "{}".format(self.value)

    def __repr__(self):
        """
        Description:
            Repr representation of Node Object
        :return:
            A String, which actually represents the node.
            If this string executed, Same Node will be created again.
        Examples:
            Please refer __init__ method examples
        """
        next_node = None
        if self.next_node:
            next_node = "Node({})".format(self.next_node)
        return "Node(value={}, next_node={})".format(self.value, next_node)


class SingleLinkedList:
    """
    Description:
        Represents Single linked list.
        For more information about Single linked list,
        please refer here - https://en.wikipedia.org/wiki/Linked_list#Singly_linked_lists
    Attributes:
        add: Adds a node to the linked list.
        head: Represents the Head of a linked list.
        get_reversed_list: Gives a new single linked list which is reversal of
                           actual linked list.
        to_number: Converts linked list to a number
        from_number: Converts number to Single linked list
    """

    def __init__(self):
        self._head = None
        self._pointer = None
        self._temp_pointer = None
        self._length = 0

    def add(self, node):
        """
        Description:
            Adds a new node to the tail of a linked list
        :param node:
            A Node type Object
        :return:
            Details of linked list as below -
                Head: Head of the linked list
                Pointer: Pointer to the tail of linked list
                Length: Length of the linked list
                LinkedList: Linked list representation with "->" as connector between nodes
        Examples:
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
        """
        if not self.head:
            self.head = node
            self._pointer = node
        else:
            self._pointer.next_node = node
            self._pointer = self._pointer.next_node
        self._length = self._length + 1
        return str(self)

    @property
    def head(self):
        """
        Description:
            Head of linked list
        :return:
            Head of a linked list
        """
        return self._head

    @head.setter
    def head(self, node):
        """
        Description:
            Setter for linked list head
        :param node:
            Object of type Node
        :return:
            None
        """
        self._head = node
        self._temp_pointer = node

    def __iter__(self):
        self.temp_pointer = self.head
        return self

    def __next__(self):
        if not self.temp_pointer:
            raise StopIteration
        node = self.temp_pointer
        self.temp_pointer = self.temp_pointer.next_node
        return node

    def __str__(self):
        """
        Description:
            String representation of a linked list, which shows properties of
            linked list
        :return:
            A string, which has all properties of linked list
        Examples:
            Please refer the examples of add method
        """
        return "Head: {}{}Pointer: {}{}Length: {}{}LinkedList: {}".format(self._head,
                                                                          chr(10),
                                                                          self._pointer,
                                                                          chr(10),
                                                                          self._length,
                                                                          chr(10),
                                                                          "->".join([str(node) for node in self]))

    def __len__(self):
        """
        Description:
            Length of linked list
        :return:
            linked list length
        """
        return self._length

    def __add__(self, other):
        """
        Description:
            Adds two single linked lists and produce a new linked list.
        Approach:
            1.) As addition should start from LSB(least significant bit), first we
            reverse the linked list.
            2.) Get the node of both linked list while traversing the reversed
            linked list.
            3.) Add both values of nodes,
                    Get the result. Just like the way in normal addition,
                    take out the carry forwarded value and pass to the next digit
                    i.e.
                        3 + 4 ==> 7 & carry forward is 0
                        6 + 7 ==> 3 & carry forward is 1
                        5 + 0 ==> 5 & carry forward is 0
            4.) Create a node from result "value" and add this node to linked list.
                    26 + 39 ==>
                            A.) 6 + 9 ==> 5 & carry forward is 1
                                Create a Node with value of 5
            5.) Pass the carry forwarded to the next digit,
                    26 + 39 ==>
                            B.) 2 + 3 + 1(carry forwarded from previous) ==> 6
                                Do note, here the carry forward is 0
            6.) Continue step 3, step 4, step 5 till you exhaust traversing both
                the linked lists.
            7.) And then reverse the list as we started adding the nodes
                from lsb, ideally it should be from hsb.
        :param other:
            Accepts another object of type linked list
        :raises
            Type error if other is not of type single linked list.
        :return:
            A new linked list which is summation of given linked lists.

        Examples:
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
        """
        if not isinstance(other, SingleLinkedList):
            raise TypeError("Only linked list is Acceptable.")

        first_linked_list = iter(self.get_reversed_list())
        second_linked_list = iter(other.get_reversed_list())

        summed_linked_list = SingleLinkedList()

        carry_forward = 0
        while True:
            node_in_linked_list_1 = self._get_next_value_from_iterator(first_linked_list)
            node_in_linked_list_2 = self._get_next_value_from_iterator(second_linked_list)
            if node_in_linked_list_1 is None and node_in_linked_list_2 is None:
                break
            new_number = self._nvl(node_in_linked_list_1)+self._nvl(node_in_linked_list_2)+carry_forward
            carry_forward, new_node_value = divmod(new_number, 10)
            summed_linked_list.add(Node(new_node_value))

        if carry_forward != 0:
            summed_linked_list.add(Node(carry_forward))

        return summed_linked_list.get_reversed_list()

    @staticmethod
    def _get_next_value_from_iterator(iterator):
        try:
            return next(iterator).value
        except StopIteration:
            return None

    @staticmethod
    def _nvl(value):
        if value is None:
            return 0
        return value

    def get_reversed_list(self):
        """
        Description:
            Generates a new linked list which is reverse of the actual
            linked list.
        :return:
            A new linked list which is reverse of actual linked list
        Examples:
            >>> print (new_linked_list)
            Head: 1
            Pointer: 2
            Length: 4
            LinkedList: 1->2->8->2

            >>> print (new_linked_list.get_reversed_list())
            Head: 2
            Pointer: 1
            Length: 4
            LinkedList: 2->8->2->1
        """
        reversed_list = deepcopy(self)
        current = reversed_list.head
        reversed_list._pointer = current
        next_node = current.next_node
        current.next_node = None

        while next_node:
            tmp = next_node.next_node
            next_node.next_node = current
            current = next_node
            next_node = tmp

        self._pointer = current
        reversed_list.head = current
        return reversed_list

    @classmethod
    def from_number(cls, number):
        """
        Description:
            Generates a linked list from a positive integer
        :param number:
            Accepts only positive integer
        :return:
            A new linked list
        Examples:
            >>> linked_list = SingleLinkedList.from_number(456123)

            >>> print (linked_list)
            Head: 4
            Pointer: 3
            Length: 6
            LinkedList: 4->5->6->1->2->3

        """
        if not isinstance(number, int):
            raise TypeError("Expecting only integers")
        if number < 0:
            raise ValueError("Expecting positive integers")
        single_linked_list = cls()
        single_linked_list._populate_linked_list(number)
        return single_linked_list

    def _populate_linked_list(self, number):
        new_number = number//10
        if number < 10:
            self.add(Node(int(number)))
            return
        else:
            self._populate_linked_list(new_number)
        self.add(Node(number % 10))

    def to_number(self):
        """
        Description:
            Converts linked list to an integer
        :return:
            An integer, which represents linked list
        Examples:
            >>> linked_list = SingleLinkedList.from_number(456123)

            >>> print (linked_list)
            Head: 4
            Pointer: 3
            Length: 6
            LinkedList: 4->5->6->1->2->3

            >>> linked_list.to_number()
            456123
        """
        result = 0
        for node in self:
            result = (result*10)+node.value
        return result

