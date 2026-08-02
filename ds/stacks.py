from linked_lists import DoublyLinkedList
from test import testing

class Stack:
    def __init__(self, first_elem=None):
        self._doubly_list = DoublyLinkedList()

        if first_elem is not None:
            self.push(first_elem)

    def size(self):
        return self._doubly_list.size

    def isEmpty(self):
        return self._doubly_list.size == 0

    def push(self, element):
        self._doubly_list.add_last(element)

    def pop(self):
        if self.isEmpty():
            raise Exception("List Empty!")
        
        return self._doubly_list.remove_last()

    def peek(self):
        if self.isEmpty():
            raise Exception("List Empty!")

        return self._doubly_list.peek_last()


# TESTS 
empty = Stack()
not_empty = Stack(4)

# size
testing(string_array=["Testing size of not_empty", "Testing size of empty"], data_array=[not_empty.size(),empty.size()])

# isEmpty
testing(string_array=["Testing isEmpty on not_empty", "Testing isEmpty on empty"], data_array=[not_empty.isEmpty(),empty.isEmpty()])

# push
empty.push(5)
not_empty.push(5)

# peek
testing(string_array=["Testing peek and push on not_empty", "Testing peek and push on empty"], data_array=[not_empty.peek(),empty.peek()])

# pop
testing(string_array=["Testing pop on not_empty", "Testing pop on empty"], data_array=[not_empty.pop(),empty.pop()])