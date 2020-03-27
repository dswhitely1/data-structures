import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def __len__(self):
        return self.storage.length

    def enqueue(self, value):
        self.storage.add_to_head(value)

    def dequeue(self):
        if not self.storage.head:
            return
        return self.storage.remove_from_tail()

