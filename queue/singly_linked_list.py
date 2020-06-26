
class Node: 
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
 

class LinkedList: 
    def __init__(self):
        self.head = None
        self.tail = None 
    
    def add_to_head(self, value):
        # create a node to add
        new_node = Node(value)
        # check if the list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # point new_node to current head
            new_node.next_node = self.head
            # move head to new node
            self.head = new_node
    
    def add_to_tail(self, value):
        # create a node to add
        new_node = Node(value)
        # check if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
        # point the node at the current tail, to the new node
            self.tail.next_node = new_node
            self.tail = new_node
 
    # remove the head and return its value
    def remove_head(self):
        # if list is empty, do nothing
        if not self.head:
            return None
        # if list only has one element, set head and tail to None
        if self.head.next_node is None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            return head_value
        # Otherwise we have more elements in the list
        head_value = self.head.value
        self.head = self.head.next_node
        return head_value
 
    def contains(self, value):
        if self.head is None:
            return None
 
        # Loop through each node
        current_node = self.head
 
        while current_node is not None:
            # check if this is the node we are looking for
            if current_node.value == value:
                return True
            # otherwise, go to the next node
            current_node = current_node.next_node
        return False

    def get_max(self):
        max = None
        new_node = self.head

        while new_node is not None:
            if max is None:
                max = new_node.value
            elif new_node.value > max:
                max = new_node.value

            new_node = new_node.next_node
        return max