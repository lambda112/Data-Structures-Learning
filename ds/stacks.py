from linked_lists import DoublyLinkedList as dlist
from test import Testing

class Stack:
    def __init__(self, first_elem=None):
        self.list = dlist()

        if first_elem is not None:
            self.push(first_elem)

    def size(self):
        return self.list.size

    def isEmpty(self):
        return self.list.size == 0

    def push(self, element):
        self.list.add_last(element)

    def pop(self):
        if self.isEmpty():
            raise Exception("List Empty!")
        
        return self.list.remove_last()

    def peek(self):
        if self.isEmpty():
            raise Exception("List Empty!")

        return self.list.peek_last()


# TESTS 
empty = Stack()
not_empty = Stack(4)
test = Testing

# size
test.display_results(string_array=["Testing size of not_empty", "Testing size of empty"], data_array=[not_empty.size(),empty.size()])

# isEmpty
test.display_results(string_array=["Testing isEmpty on not_empty", "Testing isEmpty on empty"], data_array=[not_empty.isEmpty(),empty.isEmpty()])

# push
empty.push(5)
not_empty.push(5)

# peek
test.display_results(string_array=["Testing peek and push on not_empty", "Testing peek and push on empty"], data_array=[not_empty.peek(),empty.peek()])

# pop
test.display_results(string_array=["Testing pop on not_empty", "Testing pop on empty"], data_array=[not_empty.pop(),empty.pop()])