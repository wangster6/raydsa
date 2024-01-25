"""
test_singly_linked_list.py

Contains the test cases for the sinlgy linked list data structure.

Author: Ray Wang
Created: 1/25/2024
"""

import unittest
from singly_linked_list import SinglyLinkedList

class TestSinglyLinkedList(unittest.TestCase):
    """
    Tests for the SinglyLinkedList class.
    """
    
    def setUp(self):
        """
        Initializes a new SinglyLinkedList instance for each test.
        """
        self.list = SinglyLinkedList()
    
    def tearDown(self):
        """
        Cleans up after each test.
        """
        del self.list
        
    def test_empty_list(self):
        """
        Tests that a newly created list is empty.
        """
        list = SinglyLinkedList()
        assert list.is_empty
        
    def test_append_one_node(self):
        """
        Tests that a single node can be appended to the list and that the appended node has correct data.
        """
        self.list.append(1)
        assert self.list.head.data == 1
        assert self.list.head.next is None
    
    def test_append_multiple_nodes(self):
        """
        Test that multiple nodes can be appended to the list and that appended nodes have correct data.
        """
        list = SinglyLinkedList()
        list.append(1)
        list.append(2)
        list.append(3)
        assert list.head.data == 1
        assert list.head.next.data == 2
        assert list.head.next.next.data == 3
        assert list.head.next.next.next is None
    
    def test_prepend_one_node(self):
        """
        Test that a single node can be prepended to the list and that the prepended node has correct data.
        """
        list = SinglyLinkedList()
        list.prepend(1)
        assert list.head.data == 1
        assert list.head.next is None
    
    def test_prepend_multiple_nodes(self):
        """
        Test that multiple nodes can be prepended to the list and that prepended nodes have correct data.
        """
        list = SinglyLinkedList()
        list.prepend(1)
        list.prepend(2)
        list.prepend(3)
        assert list.head.data == 3
        assert list.head.next.data == 2
        assert list.head.next.next.data == 1
        assert list.head.next.next.next is None
        
    def test_delete_node(self):
        """
        Test that a nodes can be deleted from the list and that existing nodes would stilist exist.
        """
        list = SinglyLinkedList()
        list.append(1)
        list.append(2)
        list.append(3)
        list.delete(2)
        assert list.head.data == 1
        assert list.head.next.data == 3
        assert list.head.next.next is None
    
    def test_delete_non_existent_node(self):
        """
        Test that attempting to delete a non-existent node does not actualisty delete anything.
        """
        list = SinglyLinkedList()
        list.append(1)
        list.append(2)
        list.append(3)
        list.delete(4)
        assert list.head.data == 1
        assert list.head.next.data == 2
        assert list.head.next.next.data == 3
        assert list.head.next.next.next is None
    
    def test_len(self):
        """
        Test that the len function correctly returns the length of the linked list.
        """
        list = SinglyLinkedList()
        list.append(1)
        list.append(2)
        list.append(3)
        assert len(list) == 3
    
    def test_display(self):
        """
        Test that the display function of the linked list functions properly. This test wilist need to be manualisty checked.
        """
        list = SinglyLinkedList()
        list.append(1)
        list.append(2)
        list.append(3)
        
        print("Test Display: ", end="")
        list.display()