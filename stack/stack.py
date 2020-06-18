"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
# 1. Implement the Stack class using an array as the underlying storage structure.
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.append(value)
        
#     def pop(self):
#         if len(self) > 0:
#             return self.storage.pop()
#         else:
#             return None

# 2. Re-implement the Stack class, this time using the linked list implementation as the underlying storage structure.
class Node: 
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node
 

class Stack: 
    def __init__(self):
        self.size = 0
        self.head = None 
        self.tail = None 

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return 
        self.tail.next_node = new_node
        self.tail = new_node
        
    def pop(self):
        if self.size == 0:
            return None
        pop_node = self.tail
        current_node = self.head

        if pop_node is not current_node:
            while current_node.next_node is not pop_node:
                current_node = current_node.next_node

        current_node.next_node = None
        self.tail = current_node
        self.size -= 1

        if self.size == 0:
            self.head = None
        return pop_node.value

    # 3. What is the difference between using an array vs. a linked list when implementing a Stack?
    # Answer - it is easier when using an array, less code.