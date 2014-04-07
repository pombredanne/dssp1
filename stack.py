import linked_list

class Stack(object):
    def __init__(self):
        self.items = linked_list.DoublyLinkedList()

    def push(self, value):
        self.items.add_last(value)

    def peek(self):
        pass

    def pop(self):
        pass
