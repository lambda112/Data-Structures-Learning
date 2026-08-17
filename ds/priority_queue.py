from test import Testing

class PQ:
    def __init__(self, sz: int = 1, elems = None):

        # initial setup of heap and map
        self.heap_size = 0
        self.heap_capacity = sz
        self.heap: list = []
        self.map: dict[any, set[int]] = {}

        # Check to see if user provided a list of elems
        if elems is not None:
            self.heap = list(elems)
            self.heap_size = len(elems)
            self.heap_capacity = max(sz, self.heap_size)

            # Minus size from heap capacity as not every element will be none
            # Append none to empty slots, so future code works without errors
            for i in range(self.heap_capacity - self.heap_size):
                self.heap.append(None)

            # Add heap value as key and index inside set as value to map
            for i in range(self.heap_size):
                self.map_add(self.heap[i], i)

            # Ensure elements satisfy heap invarient through heapify
            for i in range(max(0, (self.heap_size // 2)-1), -1, -1):
                self.sink(i)

        # If no elems are passed
        else:
            self.heap_capacity = sz
            self.heap = [None] * sz


    def is_empty(self) -> bool:
        """Checks if heap is empty returns bool"""
        return self.heap_size == 0
    

    def size(self):
        """Returns current size of heap"""
        return self.heap_size
    

    def clear(self):
        """Clears the heap and map"""
        self.heap.clear()
        self.heap_size = 0 
        self.map.clear()


    def peek(self):
        """Returns root node of heap, the first element"""
        if self.is_empty(): 
            return None
        
        return self.heap[0]
    

    def poll(self):
        """Removes and returns the root node of heap, the first element"""
        return self.remove_at(0)
    

    def contains(self, elem):
        """Check if elem is contained in map / heap"""
        if elem is None: 
            return False
        
        return elem in self.map
    

    def add(self, elem):
        """Add a new element to the heap and map"""
        # Raise error if none
        if elem is None:
            raise ValueError("Value cannot be None.")

        # Check if heap size smaller than capacity
        if (self.heap_size < self.heap_capacity):
            # Add element where heap size is
            self.heap[self.heap_size] = elem

        else:
            # Add at the end of heap and increase the capacity to match
            self.heap.append(elem)
            self.heap_capacity += 1

        # Add to map as well
        self.map_add(elem, self.heap_size)

        # Swim up the heap to satisfy invariant 
        self.swim(self.heap_size)

        # increase heap size to match
        self.heap_size += 1


    def less(self, a:int, b:int) -> bool:
        """Checks which node is smaller from passed integers"""
        node1 = self.heap[a]
        node2 = self.heap[b]

        return node1 <= node2
    

    def swim(self, k: int):
        """Swims nodes upwards until at top of heap or heap invariant is satisfied"""
        # Get parent of node k (0 based index)
        parent: int = (k-1) // 2

        # While k is not at root node and heap invariant is still not satisfied
        while k > 0 and self.less(k, parent):
            # swap the parent with k 
            self.swap(parent, k)

            # k is now where parent is
            k = parent

            # get k parents again
            parent = (k-1) // 2


    def sink(self, k:int):
        """Swims node downwards until at end of heap or heap invariant is satisfied"""
        while True:
            left: int = 2 *  k + 1 # left node
            right: int = 2 *  k + 2 # right node
            smallest: int = left # default to left 

            # if right node exists and smaller than left node, make right smallest
            if right < self.heap_size and self.less(right, left):
                smallest = right

            # check if left is in bounds or if heap invariant is satfisfied
            if left >= self.heap_size or self.less(k, smallest): 
                break

            # swap smallest and k
            self.swap(smallest, k)

            # k is now smallest
            k = smallest


    def swap(self, a: int, b: int):
        """Swap two elements/node when swimming or sinking"""
        a_elem  = self.heap[a]
        b_elem  = self.heap[b]

        self.heap[a] = b_elem
        self.heap[b] = a_elem

        self.map_swap(a_elem, b_elem, a, b)


    def remove(self, element):
        """Remove an element from the heap and map"""
        if (element is None): 
            return False

        # get set of values which hold indices
        set_index: set = self.map.get(element)

        # if set is not empty
        if set_index is not None:
            # set index is set, only need one random index, 
            # https://stackoverflow.com/questions/59825/how-to-retrieve-an-element-from-a-set-without-removing-it
            index = next(iter(set_index))
            self.remove_at(index)

        return set_index is not None
        

    def remove_at(self, i: int):
        """Remove an element at specified index from map and heap"""
        if self.is_empty() or i >= self.heap_size:
            return None

        # reduce heap size as removing from heap
        self.heap_size -= 1

        # store removed data so it can be returned
        removed_data = self.heap[i]

        # move value to be removed to end of heap
        self.swap(i, self.heap_size)

        #then remove the value from map
        self.map_remove(removed_data, self.heap_size)

        # cleared reference to prevent memory leaks
        self.heap[self.heap_size] = None

        # if last element has been removed no need to rebalance heap values 
        if (i == self.heap_size): 
            return removed_data

        # sink or swim until heap invariant is satisfied
        elem = self.heap[i]
        self.sink(i)

        if (self.heap[i] == elem):
            self.swim(i)

        return removed_data


    def map_add(self, elem, index: int) -> None:
        """Add element to map"""

        # if elem not in map, add key to dict with value as empty set
        if elem not in self.map:
            self.map[elem] = set()

        # add index value to corresponding set key
        self.map[elem].add(index)


    def map_remove(self, elem, index: int) -> None:
        "Remove element from map"

        # check if elem is in map
        if elem in self.map:

            # remove value from map
            self.map[elem].discard(index)

            # if set is empty remove from dict
            if not self.map[elem]:
                del self.map[elem] 


    def map_swap(self, elem1, elem2, index1, index2):
        """Swap values around in map when swimming or sinking"""
        self.map[elem1].discard(index1)
        self.map[elem2].discard(index2)

        self.map[elem1].add(index2)
        self.map[elem2].add(index1)


# TESTING
pq_elem = PQ(5, [10,20,30,40])
pq = PQ(5)
test = Testing

# size
test.display_results(string_array=["Testing size of pq", "Testing size of pq_elem"], data_array=[pq.size(),pq_elem.size()])

# is_empty
test.display_results(string_array=["Testing is_empty pq", "Testing is_empty pq_elem"], data_array=[pq.is_empty(),pq_elem.is_empty()])

# peek
test.display_results(string_array=["Testing peek pq", "Testing peek pq_elem"], data_array=[pq.peek(),pq_elem.peek()])

# poll 

## used to get copy instead of live reference
old_val = [
    [list(pq.heap), {k: set(v) for k, v in pq.map.items()}], 
    [list(pq_elem.heap), {k: set(v) for k, v in pq_elem.map.items()}]
]

test.display_results(string_array=["Testing poll pq", "Testing poll pq_elem"], data_array=[pq.poll(),pq_elem.poll()])

new_val = [
    [list(pq.heap), {k: set(v) for k, v in pq.map.items()}], 
    [list(pq_elem.heap), {k: set(v) for k, v in pq_elem.map.items()}]
]

test.display_changes(old_values= old_val, new_values=new_val, var_values=["pq heap", "pq map","pq_elem heap", "pq_elem map"])


# contains
test.display_results(string_array=["Testing contains pq", "Testing contains pq_elem"], data_array=[pq.contains(30),pq_elem.contains(30)])


# add
old_val = [
    [list(pq.heap), {k: set(v) for k, v in pq.map.items()}], 
    [list(pq_elem.heap), {k: set(v) for k, v in pq_elem.map.items()}]
]

test.display_results(string_array=["Testing add pq", "Testing add pq_elem"], data_array=[pq.add(50),pq_elem.add(50)])

new_val = [
    [list(pq.heap), {k: set(v) for k, v in pq.map.items()}], 
    [list(pq_elem.heap), {k: set(v) for k, v in pq_elem.map.items()}]
]

test.display_changes(old_values= old_val, new_values=new_val, var_values=["pq heap", "pq map","pq_elem heap", "pq_elem map"])


# remove
old_val = [
    [list(pq.heap), {k: set(v) for k, v in pq.map.items()}], 
    [list(pq_elem.heap), {k: set(v) for k, v in pq_elem.map.items()}]
]

test.display_results(string_array=["Testing remove pq", "Testing remove pq_elem"], data_array=[pq.remove(20),pq_elem.remove(20)])

new_val = [
    [list(pq.heap), {k: set(v) for k, v in pq.map.items()}], 
    [list(pq_elem.heap), {k: set(v) for k, v in pq_elem.map.items()}]
]

test.display_changes(old_values= old_val, new_values=new_val, var_values=["pq heap", "pq map","pq_elem heap", "pq_elem map"])


# remove_at
old_val = [
    [list(pq.heap), {k: set(v) for k, v in pq.map.items()}], 
    [list(pq_elem.heap), {k: set(v) for k, v in pq_elem.map.items()}]
]

test.display_results(string_array=["Testing remove_at pq", "Testing remove_at pq_elem"], data_array=[pq.remove_at(1),pq_elem.remove_at(1)])

new_val = [
    [list(pq.heap), {k: set(v) for k, v in pq.map.items()}], 
    [list(pq_elem.heap), {k: set(v) for k, v in pq_elem.map.items()}]
]

test.display_changes(old_values= old_val, new_values=new_val, var_values=["pq heap", "pq map","pq_elem heap", "pq_elem map"])


# clear
old_val = [
    [list(pq.heap), {k: set(v) for k, v in pq.map.items()}], 
    [list(pq_elem.heap), {k: set(v) for k, v in pq_elem.map.items()}]
]

test.display_results(string_array=["Testing clear pq", "Testing clear pq_elem"], data_array=[pq.clear(),pq_elem.clear()])

new_val = [
    [list(pq.heap), {k: set(v) for k, v in pq.map.items()}], 
    [list(pq_elem.heap), {k: set(v) for k, v in pq_elem.map.items()}]
]

test.display_changes(old_values= old_val, new_values=new_val, var_values=["pq heap", "pq map","pq_elem heap", "pq_elem map"])