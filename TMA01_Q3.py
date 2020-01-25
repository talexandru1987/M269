#!/usr/bin/env python3
"""
Code file for M269 19J TMA01 Question 3

Student version 1: 7/3/19
"""

# Part (a)

def is_sorted(numbers):
    """Return True if numbers is sorted in ascending order, otherwise False.

    Assume numbers is a list of integer values.
    """
    n = len(numbers)
    state = True
    if n == 1:
        return state
    else:
        for index in range (1, len(numbers)):
            currentvalue = numbers[index]
            position = index
            while position > 0 and numbers[position -1] > currentvalue:
                position = 0
                state = False   
        return state        
# Part (b)


def is_palindrome(the_list):
    """Return True if the_list is a palindromic list, otherwise False."""

    for i in range(0, len(the_list)//2):
        if the_list[i] != the_list[len(the_list)- i -1]:
            return False
    return True

    

