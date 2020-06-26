from queue import Queue

"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value: 
            if self.left:
                self.left.insert(value)
            else: 
                self.left = BSTNode(value)

        if value >= self.value:
            if self.right:
                self.right.insert(value)
            else: 
                self.right = BSTNode(value)           


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True

        found = False
        if self.value >= target:
            if self.left is None:
                return False
            found = self.left.contains(target)
        else:
            if self.right is None:
                return False
            found = self.right.contains(target)
        return found


    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)

        if self.right:
            self.right.for_each(fn)          

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node): # (Left, Root, Right)
        if self.left:
            self.left.in_order_print(self.left)
        
        print(self.value)
        if self.right:
            self.right.in_order_print(self.right)


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # create a queue for nodes
        queue = Queue()
        # add the first node to the queue
        queue.enqueue(node)

        # while queue is not empty
        while queue.size > 0:
            # remove the first node from the queue
            current_node = queue.dequeue()
            # print the removed node 
            print(current_node.value)

            # add all the children into the queue
            if current_node.left is not None:
                queue.enqueue(current_node.left)
            if current_node.right is not None:
                queue.enqueue(current_node.right)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):  
        array = []     
        # add the first node  
        array.append(node)

        # while array is not empty
        while len(array) > 0:
            # get the current node
            current_node = array.pop()
            # print that node
            print(current_node.value)

            # add all the children to the array
            if current_node.right is not None:
                array.append(current_node.right)
            if current_node.left is not None:
                array.append(current_node.left)
              

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)
        if node.left:
            self.pre_order_dft(node.left)

        if node.right:
            self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left:
            self.post_order_dft(node.left)

        if node.right:
            self.post_order_dft(node.right)
        print(node.value)


# testing and printing--------------------------
root_node = BSTNode(10)
root_node.insert(5)
root_node.insert(7)
root_node.insert(2)
root_node.insert(12)
root_node.insert(11)
root_node.insert(22)

# const print_node = (x) => { console.log(x) }
print_node = lambda x: print(f'current_node is : {x}')

root_node.for_each(print_node)
print("")

print(f'Print all the values in order from low to high: ')
root_node.in_order_print(print_node)
print("")

print(f'bft_print')
print(root_node.bft_print(root_node))
print("")

print(f'dft_print')
print(root_node.dft_print(root_node))
print("")

print(f'pre_order_dft (Root, Left, Right)')
print(root_node.pre_order_dft(root_node))
print("")

print(f'post_order_dft (Left, Right, Root)')
print(root_node.post_order_dft(root_node))
print("")