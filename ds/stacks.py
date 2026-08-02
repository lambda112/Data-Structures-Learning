from linked_lists import DoublyLinkedList

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

