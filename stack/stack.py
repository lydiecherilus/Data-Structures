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
#         return self.size

#     def push(self, value):
#         self.size += 1
#         self.storage.insert(0, value)
        
#     def pop(self):
#         if len(self.storage) > 0:
#             self.size -= 1
#             return self.storage.pop(0)
#         else:
#             return None

# 2. Re-implement the Stack class, this time using the linked list implementation as the underlying storage structure.
from singly_linked_list import LinkedList

class Stack: 
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        self.storage.add_to_head(value)

    def pop(self):
        if self.size == 0:
            return None
        else: 
            self.size -= 1
            return self.storage.remove_head()

    # 3. What is the difference between using an array vs. a linked list when implementing a Stack?
    # Answer - it seems to be easier and less code when using an array at first but after importing LinkedList from singly_linked_list and used it,
    # the implementing with a linked list is way simpler and more efficient.