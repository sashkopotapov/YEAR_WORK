
class AbstractCollection(object):
    """An abstract collection implementation."""

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    # Accessor methods
    def __len__(self):
        """-> The number of items in self."""
        return self._size

    def isEmpty(self):
        return len(self) == 0

    def __str__(self):
        """Returns the string representation of self."""
        return "[" + ", ".join(map(str, self)) + "]"

    def __add__(self, other):
        """Returns a new collection consisting of the
        items in self and other."""
        result = type(self)(self)
        for item in other:
            result.add(item)
        return result

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        if self is other: return True
        if type(self) != type(other) or \
           len(self) != len(other):
            return False
        otherIter = iter(other)
        for item in self:
            if item != next(otherIter):
                return False
        return True


class Node(object):
    """Nodes for singly linked structures."""

    def __init__(self, data, next = None):
        """Instantiates a Node with default next of None"""
        self.data = data
        self.next = next


class LinkedQueue (AbstractCollection):
    """A link-based queue implementation."""

    # Constructor
    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._front = self._rear = None
        AbstractCollection.__init__ (self, sourceCollection)

    # Accessor methods
    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = self._front
        while not cursor is None:
            yield cursor.data
            cursor = cursor.next

    def peek(self):
        """
        Returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if the stack is empty."""
        if self.isEmpty ():
            raise KeyError ("The queue is empty.")
        return self._front.data

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._size = 0
        self._front = self._rear = None

    def add(self, item):
        """Adds item to the rear of the queue."""
        newNode = Node (item, None)
        if self.isEmpty ():
            self._front = newNode
        else:
            self._rear.next = newNode
        self._rear = newNode
        self._size += 1

    def pop(self):
        """
        Removes and returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if the queue is empty.
        Postcondition: the front item is removed from the queue."""
        if self.isEmpty ():
            raise KeyError ("The queue is empty.")
        oldItem = self._front.data
        self._front = self._front.next
        if self._front is None:
            self._rear = None
        self._size -= 1
        return oldItem

    def remove(self, index):
        """Removes and returns the item at index,
        where index ranges from 0 (the front) to size - 1 (the rear).
        Precondition: 0 <= index < size of queue"""
        if index < 0 or index >= len (self):
            raise AttributeError ("i must be >= 0 and < size of queue")
        if index == 0:
            oldItem = self._front.data
            self._front = self._front.next
        else:
            probe = self._front
            while index > 1:
                probe = probe.next
                index -= 1
            oldItem = probe.next.data
            probe.next = probe.next.next
        self._size -= 1
        if self.isEmpty ():
            self._rear = None
        return oldItem


