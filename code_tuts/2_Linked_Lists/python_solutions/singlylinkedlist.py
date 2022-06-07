#!/bin/python3
# Author: Sebastian Opiyo
# Date Created: June 07, 2022
# Description: Linked Lists implementation, Python3 Version.


class Node:
    """Creates a NODE; a data container and initiates pointers."""

    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.count = 0

    # Helper methods
    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

    def increase_count(self):
        self.count += 1

    def decrease_count(self):
        self.count -= 1


class LinkedList:
    """Create all the methods that we use to operationalize the LL."""

    def __init__(self):
        self._head = None
        self._curr = None
        self._tail = None

    def is_empty(self):
        return self._head is None

    def add_to_head(self, data):
        new_node = Node(data)
        pass

    def remove_from_head(self):
        pass

    def reset_head(self):
        pass

    def move_forward(self):
        pass

    def add_after_current(self):
        pass

    def remove_after_current(self):
        pass

    def find(self, value):
        pass

    def delete(self, value):
        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass
