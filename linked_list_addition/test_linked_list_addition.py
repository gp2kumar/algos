import unittest
from linked_list_addition import Node, SingleLinkedList


class TestSingleLinkedList(unittest.TestCase):

    def test_single_linked_list(self):
        single_linked_list = SingleLinkedList()
        single_linked_list.add(Node(1))
        self.assertEqual(len(single_linked_list), 1)

    def test_single_linked_list_add(self):
        single_linked_list = SingleLinkedList()
        single_linked_list.add(Node(1))
        single_linked_list.add(Node(2))
        single_linked_list.add(Node(3))
        print(single_linked_list)
        self.assertEqual(len(single_linked_list), 3)

    def test_single_linked_list_reverse(self):
        single_linked_list = SingleLinkedList()
        single_linked_list.add(Node(1))
        single_linked_list.add(Node(2))
        single_linked_list.add(Node(3))
        single_linked_list.add(Node(4))
        single_linked_list.add(Node(9))
        reversed_list = single_linked_list.get_reversed_list()
        self.assertIn("9->4->3->2->1", str(reversed_list))
        reversed_list.add(Node(7))
        self.assertIn("9->4->3->2->1->7", str(reversed_list))
        self.assertEqual(reversed_list.head.value, 9)

    def test_single_linked_list_sum(self):
        linked_list1 = SingleLinkedList()
        linked_list2 = SingleLinkedList()
        linked_list1.add(Node(9))
        linked_list1.add(Node(9))
        linked_list1.add(Node(9))
        linked_list2.add(Node(9))
        linked_list2.add(Node(9))
        linked_list2.add(Node(9))

        new_linked_list = linked_list1 + linked_list2
        print(new_linked_list)

    def test_single_linked_list_from_number(self):
        number = 1234567890
        linked_list = SingleLinkedList.from_number(number)
        number_as_linked_list = "->".join([c for c in str(number)])
        self.assertIn(number_as_linked_list, str(linked_list))

    def test_to_number(self):
        number = 1234
        linked_list = SingleLinkedList.from_number(number)
        self.assertEqual(linked_list.to_number(), number)

    def test_two_linked_list_addition(self):
        ll1 = SingleLinkedList.from_number(123)
        ll2 = SingleLinkedList.from_number(456342)
        ll3 = SingleLinkedList.from_number(1000)
        new_ll = ll1+ll2+ll3
        self.assertEqual(new_ll.to_number(), 123+456342+1000)

    def test_two_linked_list_addition_with_incorrect_linked_list(self):
        ll1 = SingleLinkedList.from_number(123)
        self.assertRaises(TypeError, lambda: ll1+1)
