# -*- coding: utf-8 -*-
import linked_list

class Stack(object):
    """
    All operations on a stack are O(1)
    """
    def __init__(self):
        self.items = linked_list.DoublyLinkedList()

    def push(self, value):
        self.items.add_last(value)

    def peek(self):
        if not self.items.count:
            raise Exception("Cannot peek at an empty stack ☹")
        return self.items._tail.value

    def pop(self):
        if not self.items.count:
            raise Exception("Cannot pop from an empty stack ☹")
        tail_value = self.items._tail.value
        self.items.remove_last()
        return tail_value

    def get_count(self):
        return self.items.count

