"""
Library file for M269 18J TMA01 Question 4

Version 1: 7/3/19
Version 2: 18/11/19     corrected the Stack's documentation string
"""


class Stack:
    """
    An implementation of stacks, following Miller and Ranum Section 3.3

    A Last-in First-out (LIFO) collection of items.
    """

    def __init__(self):
        """ Initialise the stack to be empty. """
        self.items = []

    def isEmpty(self):
        """Return True if there are no items in the stack, otherwise False."""
        return self.items == []

    def push(self, item):
        """Add item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Return item on the top of the stack and remove it from the stack."""
        return self.items.pop()

    def peek(self):
        """Return item on the top of the stack."""
        return self.items[len(self.items)-1]

    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)
