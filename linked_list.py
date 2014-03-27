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
        Adds the provided value to the end of the linked list O(1)
        """
        node = Node(value)
        if not self._head:
            self._head = node
            self._tail = node
        else:
            self._tail.nextNode = node
            self._tail = node

        self.count += 1

    def remove(self, value):
        """
        Removes the first occurence of a node which matches the given value O(n)
        """
        previous = None
        current = self._head

        while current:
            if current.value == value:
                if previous:
                    previous.nextNode = current.nextNode
                    if not current.nextNode:
                        self._tail = previous
                else:
                    self._head = self._head.nextNode
                    if not self._head:
                        self._tail = None

                self.count -= 1
                return True

            previous = current
            current = current.nextNode

        return False

    def contains(self, value):
        """
        O(n)
        """
        current = self._head
        while current:
            if current.value == value:
                return True
            else:
                current = current.nextNode
        return False

    def __repr__(self):
        string_representation = ""
        current = self._head
        while current:
           string_representation = string_representation + str(current.value) + ","
           current = current.nextNode
        return "<LinkedList: (%s) >" % string_representation.strip(",")
