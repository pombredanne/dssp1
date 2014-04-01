class Node(object):
    """
    At the core of a linked list is a node, a container that provides the ability
    to store data and also connect to other nodes.
    """
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode


class LinkedList(object):
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

    def clear(self):
        """
        O(1)
        """
        self._head = None
        self._tail = None
        self.count = 0

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

    def __iter__(self):
        current = self._head
        while current:
            yield current
            current = current.nextNode

    def __repr__(self):
        string_representation = ""
        current = self._head
        while current:
           string_representation = string_representation + str(current.value) + ","
           current = current.nextNode
        return "<LinkedList: (%s)>" % string_representation.strip(",")


class DoublyLinkedListNode(Node):
    def __init__(self, value, nextNode=None, previousNode=None):
        super(DoublyLinkedListNode, self).__init__(value, nextNode)
        self.previousNode = previousNode

class DoublyLinkedList(LinkedList):
    def add(self, value):
        self.add_last(value)

    def add_last(self, value):
        node = DoublyLinkedListNode(value)

        if self.count:
            self._tail.nextNode = node
            node.previousNode = self._tail
        else:
            self._head = node

        self._tail = node
        self.count += 1

    def add_first(self, value):
        node = DoublyLinkedListNode(value)

        if self.count:
            self._head.previousNode = node
            node.nextNode = self._head

        self._head = node
        self.count += 1

    def remove_first(self):
        """
        O(1) - It doesn't take any more operations to reach the _head of a
        longer than a shorter list.
        """
        if self.count:
            self._head = self._head.nextNode
            self.count -= 1
            if not self.count:
                self._tail = None
            else:
                self._head.previousNode = None
            return True
        else:
            return False

    def remove_last(self):
        if self.count:
            if self.count == 1:
                self._head = None
                self._tail = None
            else:
                self._tail = self._tail.previousNode
                self._tail.nextNode = None

            self.count -= 1
            return True

        return False

