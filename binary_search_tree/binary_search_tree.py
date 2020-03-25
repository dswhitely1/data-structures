import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Create a new BST Node
        new_node = BinarySearchTree(value)

        cur_node = self.find_node(self, value)
        if cur_node.value > value:
            cur_node.left = new_node
        else:
            cur_node.right = new_node

    def find_node(self, current_node, value):
        if current_node.value > value and current_node.left is not None:
            return self.find_node(current_node.left, value)
        elif current_node.value < value and current_node.right is not None:
            return self.find_node(current_node.right, value)
        else:
            return current_node

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        found_node = self.find_node(self, target)
        if target == found_node.value:
            return True
        return False


    # Return the maximum value found in the tree
    def get_max(self):

        def max_helper(cur):
            if cur.right is None:
                return cur.value
            cur = cur.right
            return max_helper(cur)

        return max_helper(self)

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
