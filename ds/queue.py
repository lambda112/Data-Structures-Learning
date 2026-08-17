from linked_lists import DoublyLinkedList as dlist
from test import Testing

class Queue:
    def __init__(self, first_elem = None):
        self.list = dlist()

        if first_elem is not None:
            self.offer(first_elem)


    def size(self):
        """Returns size of queue"""
        return self.list.size
    

    def is_empty(self):
        """Returns true if queue is empty else false"""
        return self.list.size == 0
    

    def peek(self):
        """Returns first element in a queue"""
        if self.is_empty():
            raise Exception("Queue is Empty!")
        
        return self.list.peek_first()


    def poll(self):
        """Returns first element in queue and then removes it"""
        if self.is_empty():
            raise Exception("Queue is Empty!")

        return self.list.remove_first()


    def offer(self, value):
        """Adds element to back of the queue"""
        if value is None:
            raise Exception("Value cannot be None!")

        self.list.add_last(value)


    def __iter__(self):
        return iter(self.list)
    
# Testing
queue = Queue(7)
test = Testing

# size
test.display_results(test_string="Testing size method", test_data= queue.size())

# isEmpty
test.display_results(test_string="Testing isEmpty method", test_data= queue.is_empty())

# Peek
test.display_results(test_string="Testing peek method", test_data= queue.peek())

# Poll
test.display_results(test_string="Testing poll method", test_data= queue.poll())

# offer
queue.offer(10)
test.display_results(test_string="Testing offer method", test_data= queue.peek())

# iter
queue_iter = queue.__iter__()
queue.poll()

print("Testing iter method:")
for i in range(0,5):
    queue.offer(i)

for val in queue_iter:
    print(val)