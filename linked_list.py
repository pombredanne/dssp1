class Node:
    """
    At the core of a linked list is a node, a container that provides the ability
    to store data and also connect to other nodes.
    """
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode


class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self.count = 0

    def add(self, value):
        """
        Adds the provided value to the end of the linked list
        """
        node = Node(value)
        if not self._head:
            self._head = node
            self._tail = node
        else:
            self._tail.nextNode = node
            self._tail = node

        self.count += 1

