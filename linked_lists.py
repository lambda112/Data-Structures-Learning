class Node:
    #Internal struct like class representing a node
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None


    def __len__(self):
        return self.size


    def isempty(self):
        return self.size == 0


    def clear(self):
        trav = self.head

        while trav != None:
            next_node = trav.next
            trav.prev = None
            trav.next = None
            trav = next_node

        self.head = None
        self.tail = None
        self.size = 0


    def add_first(self, element):
        """Adds an element to the beginning of the linked list."""

        # Create new node with data that will be inputted from user
        new_node = Node(data = element)

        # If linked list empty, new node becomes head and tail
        if self.isempty():
            self.head = new_node
            self.tail = new_node

        # if linked list not empty, prev head points to new node, new node points to head
        else: 
            placeholder = self.head         # Store current head value
            self.head = new_node            # Make new node head
            new_node.next = placeholder     # Point new node to previous head value
            placeholder.prev = new_node     # Point previous head to new new node

        self.size +=1


    def add_last(self, element):
        """Adds an element to the end of the linked list (default append)."""

        # Create new node with data that will be inputted from user
        new_node = Node(data=element)

        # If linked list empty, new node becomes head and tail
        if self.isempty():
            self.head = new_node
            self.tail = new_node

        # if linked list not empty, new node becomes tail and points to previous tail, prev tail points at new node
        else:
            placeholder = self.tail         # Store current tail value
            self.tail = new_node            # Make new node tail
            placeholder.next = new_node     # Point new node to previous tail value
            new_node.prev = placeholder     # Point previous tail to new node

        self.size +=1


    def remove_first(self):
        """
        Removes the first element from the beginning of the linked list.
        
        Returns:
            The data payload that was stored inside the removed head node.
        """

        # Check if list is empty, if so raise exception
        if self.isempty(): raise Exception("List is empty!")

        else:
            # Store data to remove 
            placeholder = self.head
            data = placeholder.data

            # Adavance head pointer and decrease size of list
            self.head = placeholder.next
            self.size -= 1

            # Check if list is now empty and handle edge cases
            if self.isempty(): self.tail = None

            # remove new head previous pointer
            else: self.head.prev = None

        return data


    def remove_last(self):
        """
        Removes the last element from the end of the linked list.
        
        Returns:
            The data payload that was stored inside the removed tail node.
        """

        # Check if list is empty
        if self.isempty():
            raise Exception("List is empty!")

        else:  
            # Store data to remove
            placeholder = self.tail
            data = placeholder.data

            # Advance tail pointer and decrease size of list
            self.tail = placeholder.prev
            self.size -= 1

            # Check if list is now empty and handle edge cases
            if self.isempty(): self.head = None

            # Remove new tail next pointer
            else: self.tail.next = None

        return data


    def peek_first(self):
        """
        Peeks at the head of the list
        
        Returns:
            The data stored at head
        """

        # If list empty raise exception
        if self.isempty():
            raise Exception("List is empty!")

        # return head data
        return self.head.data


    def peek_last(self):
        """
        Peeks at the tail of the list
        
        Returns:
            The data stored at tail
        """

        # If list empty raise exception
        if self.isempty():
            raise Exception("List is empty!")

        # return tail data
        return self.tail.data


    def remove_at(self, index):
        """
        Removes element at specified index in linked list.
        
        Returns:
            The data payload that was stored inside the indexed node.
        """

        # If list empty, index too big, or index too small, raise exception
        if self.isempty() or index > self.size - 1 or index < 0:
            raise Exception("Index invalid!") 

        # if index at head return result of remove_first()
        if index == 0:
            return self.remove_first()

        # if index at tail return result of remove_last()
        elif index == self.size - 1:
            return self.remove_last() 

        else:
            # If index bigger than value of half of list size, start from tail
            if index > self.size / 2:

                # index counter decrements to check if code reaches inputted index
                index_counter = self.size - 1
                trav = self.tail

                # loop continues until index_counter is the same as index
                while index_counter != index: 
                    trav = trav.prev
                    index_counter -= 1

                # store data at index
                data = trav.data

                # fix prev and next pointers so they are pointing at each other
                trav.prev.next = trav.next
                trav.next.prev = trav.prev

            # if index is smaller than value of half of list size, start from head
            else:

                # index counter increments to check if code reaches inputted index
                index_counter = 0
                trav = self.head

                # loop continues until index_counter is the same as index
                while index_counter != index: 
                    trav = trav.next 
                    index_counter += 1

                # store data at index
                data = trav.data

                # fix prev and next pointers so they are pointing at each other
                trav.prev.next = trav.next
                trav.next.prev = trav.prev

            # decrease size of list 
            self.size -= 1
            return data


# ==========================================
# TESTING
# ==========================================

if __name__ == "__main__":
    # 1. Instantiate the list
    dll = DoublyLinkedList()
    print(f"Initial state - Is empty? {dll.isempty()}, Size: {len(dll)}")

    # 2. Test add_first
    print("\n--- Testing add_first ---")
    dll.add_first("Node B")
    dll.add_first("Node A")
    print(f"Size after add_first: {len(dll)}")
    print(f"Head data: {dll.head.data} (Expected: Node A)")
    print(f"Tail data: {dll.tail.data} (Expected: Node B)")

    # 3. Test add_last
    print("\n--- Testing add_last ---")
    dll.add_last("Node C")
    print(f"Size after add_last: {len(dll)}")
    print(f"Tail data updated to: {dll.tail.data} (Expected: Node C)")

    # 4. Test remove_first
    print("\n--- Testing remove_first ---")
    dll.remove_first()
    print(f"Size after remove_first: {len(dll)}")
    print(f"Head data updated to: {dll.head.data} (Expected: Node B)")

    # Return Node A for future tests
    dll.add_first("Node A")

    # 5. Test remove_last
    print("\n--- Testing remove_last ---")
    dll.remove_last()
    print(f"Size after remove_last: {len(dll)}")
    print(f"Tail data updated to: {dll.tail.data} (Expected: Node B)")

    # Return Node C for future tests
    dll.add_last("Node C")

    # 6. Test peak_first
    print("\n--- Testing peak_first ---")
    print(f"peak_first: {dll.peek_first()} (Expected: Node A)")

    # 7. Test peak_last
    print("\n--- Testing peak_last ---")
    print(f"peak_last: {dll.peek_last()} (Expected: Node C)")

    # Verify Pointers
    print("\n--- Verifying Forward and Backward Links ---")
    
    # Forward Traversal (A -> B -> C)
    forward_result = []
    trav = dll.head
    while trav is not None:
        forward_result.append(str(trav.data))
        trav = trav.next
    print(f"Forward check:  {' -> '.join(forward_result)}")
    print(f"Expected:       Node A -> Node B -> Node C")

    # Backward Traversal (C -> B -> A)
    backward_result = []
    trav = dll.tail
    while trav is not None:
        backward_result.append(str(trav.data))
        trav = trav.prev
    print(f"Backward check: {' -> '.join(backward_result)}")
    print(f"Expected:       Node C -> Node B -> Node A")