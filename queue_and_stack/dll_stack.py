import sys

sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def __len__(self):
        return self.storage.length

    def push(self, value):
        self.storage.add_to_head(value)

    def pop(self):
        if not self.storage.head:
            return
        return self.storage.remove_from_head()

