import unittest
import collections_and_iterators

""" Collections - TESTS 
    Testing Collections programming examples from collections.py 

    Gabby Ortman 
"""

class TestObjectMethods(unittest.TestCase): 
    def setUp(self): 
        self.singleLinkList = collections_and_iterators.SinglyLinkedList()
        
        self.singleLinkListData = collections_and_iterators.SinglyLinkedList()
        self.singleLinkListData.append("Cosmo")
        self.singleLinkListData.append("Allie")
        self.singleLinkListData.append("Watson")
        
        self.doubleLinkList = collections_and_iterators.DoublyLinkedList()
        self.doubleLinkListData = collections_and_iterators.DoublyLinkedList()

    #test that a newly initialized singly linked list has size 0, null head and null cursor
    def test_empty_single_list(self): 
        self.assertEqual(0, self.singleLinkList.size)
        self.assertIsNone(self.singleLinkList.head)
        self.assertIsNone(self.singleLinkList.cursor)

    #__contains__ should return true if the list contains specified data 
    def test_contains_success(self): 
        self.assertTrue(self.singleLinkListData.__contains__("Cosmo"))
        self.assertTrue(self.singleLinkListData.__contains__("Allie"))
        self.assertTrue(self.singleLinkListData.__contains__("Watson"))

    def test_contains_failure(self): 
        pass 

    #Append should add data to the end of the list
    def test_append(self): 
        self.assertEqual("Cosmo", self.singleLinkListData.__getitem__(0))
        self.assertEqual("Allie", self.singleLinkListData.__getitem__(1))
        self.assertEqual("Watson", self.singleLinkListData.__getitem__(2))
        with self.assertRaises(IndexError):
            self.singleLinkListData.__getitem__(3)
        self.singleLinkListData.append("Foley")
        self.assertEqual("Foley", self.singleLinkListData.__getitem__(3))

    #__getitem__ should get the data at the specified index unless the specified index is out of bounds. then it should throw an exception
    def test_getitem(self): 
        self.assertEqual("Cosmo", self.singleLinkListData.__getitem__(0))
        self.assertEqual("Allie", self.singleLinkListData.__getitem__(1))
        self.assertEqual("Watson", self.singleLinkListData.__getitem__(2))
        with self.assertRaises(IndexError):
            self.singleLinkListData.__getitem__(3) 

    #__setitem__ should change the data at a given index
    def test_setitem(self): 
        self.assertEqual("Cosmo", self.singleLinkListData.__getitem__(0))
        self.singleLinkListData.__setitem__(0, "Smalls")
        self.assertEqual("Smalls", self.singleLinkListData.__getitem__(0)) 

    #test that a newly initated doubly linked list has size 0, null head and null cursor 
    #this shouldn't be any different from the previous test, BUT, what if inheritance was done incorectly? 
    def test_empty_double_list(self): 
        self.assertEqual(0, self.doubleLinkList.size)
        self.assertIsNone(self.doubleLinkList.head)
        self.assertIsNone(self.doubleLinkList.cursor)



if __name__ == '__main__':
    unittest.main(verbosity=2)
