#!/usr/bin/env python3
"""
Code file for M269 19J TMA01 Question 4

Student version 1: 1/5/19
"""

from TMA01_Q4_stack import Stack

# Part (d)

def reverse_to_list(s):
    """Return a list containing contents of stack s in reverse order."""
    # Change the following code into an inspector
    inverted_stack = Stack()
    while not s.isEmpty():
        inverted_stack.push(s.pop())
    reversed_list = []
    while not inverted_stack.isEmpty():
        s.push(inverted_stack.peek())
        reversed_list.append(inverted_stack.pop())
    return reversed_list

# Part (e)

def is_palindrome(the_list):
    """Return True if the_list is a palindromic list, otherwise False.

    Use stack operations."""
    reversed_stack = Stack()
    if len(the_list) == 1:
        return True
    else:
        for i in range(len(the_list) - 1):
            reversed_stack.push(the_list[i])
        for i in range(len(the_list) - 1):
            if the_list[i] != reversed_stack.pop():
                return True
        return False
